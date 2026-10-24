#!/usr/bin/env python3
"""
prod-sdlc-factory validation suite.

Validates structural consistency of the factory repository:
  - YAML and JSON files parse without errors
  - Agent registry references resolve to existing files
  - Skill registry references resolve to existing files
  - Command registry references resolve to existing files
  - Capabilities registry references resolve to existing files
  - Skill SKILL.md frontmatter has required name and description fields
  - Skill directory name matches frontmatter name
  - Schema files referenced by agents exist and parse as valid JSON Schema
  - Workflow router reference exists
  - Lifecycle YAML states and transitions are self-consistent
  - Checkpoint template is valid JSON
  - No registered capability with status=available points to a missing path

Usage:
    python3 tests/validate_factory.py [--root /path/to/repo]

Exit codes:
    0  All checks passed
    1  One or more checks failed
"""

import json
import os
import re
import sys
import yaml
import argparse

PASS = "PASS"
FAIL = "FAIL"
BLOCKED = "BLOCKED"
NOT_APPLICABLE = "NOT_APPLICABLE"

results = []


def check(name, status, detail=""):
    """Record a check result."""
    results.append({"name": name, "status": status, "detail": detail})
    icon = {"PASS": "✓", "FAIL": "✗", "BLOCKED": "⊘", "NOT_APPLICABLE": "—"}.get(status, "?")
    print(f"  [{icon}] {status:16s} {name}")
    if detail and status in (FAIL, BLOCKED):
        for line in detail.strip().splitlines():
            print(f"              {line}")


def load_yaml(path):
    with open(path) as f:
        return yaml.safe_load(f)


def load_json(path):
    with open(path) as f:
        return json.load(f)


def run_all(root):
    print("\n=== prod-sdlc-factory Validation Suite ===\n")

    # -------------------------------------------------------------------------
    # 1. YAML parse validation
    # -------------------------------------------------------------------------
    print("# 1. YAML/JSON parse checks")
    yaml_errors = []
    json_errors = []
    skip_dirs = {".git", "prod-sdlc-factory-skills-and-commands", "node_modules", "__pycache__"}

    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for fname in files:
            fpath = os.path.join(dirpath, fname)
            rel = os.path.relpath(fpath, root)
            if fname.endswith(".yaml") or fname.endswith(".yml"):
                try:
                    load_yaml(fpath)
                except Exception as e:
                    yaml_errors.append(f"{rel}: {e}")
            elif fname.endswith(".json"):
                try:
                    load_json(fpath)
                except Exception as e:
                    json_errors.append(f"{rel}: {e}")

    check("All YAML files parse", FAIL if yaml_errors else PASS,
          "\n".join(yaml_errors))
    check("All JSON files parse", FAIL if json_errors else PASS,
          "\n".join(json_errors))

    # -------------------------------------------------------------------------
    # 2. Agent registry vs. filesystem
    # -------------------------------------------------------------------------
    print("\n# 2. Agent registry checks")
    agents_yaml = os.path.join(root, ".factory/registry/agents.yaml")
    if not os.path.exists(agents_yaml):
        check("agents.yaml exists", FAIL, f"Missing: {agents_yaml}")
    else:
        check("agents.yaml exists", PASS)
        agents_data = load_yaml(agents_yaml)
        agent_ids = set()
        for agent in agents_data.get("agents", []):
            aid = agent.get("id", "<no-id>")
            src = agent.get("source", "")
            abs_src = os.path.join(root, src)
            if aid in agent_ids:
                check(f"Agent id unique: {aid}", FAIL, "Duplicate agent id")
            agent_ids.add(aid)
            if src:
                check(f"Agent file exists: {src}", PASS if os.path.exists(abs_src) else FAIL,
                      f"Missing: {abs_src}" if not os.path.exists(abs_src) else "")
            else:
                check(f"Agent has source: {aid}", FAIL, "No source field")

    # -------------------------------------------------------------------------
    # 3. Skill registry vs. filesystem
    # -------------------------------------------------------------------------
    print("\n# 3. Skill registry checks")
    skills_yaml = os.path.join(root, ".factory/registry/skills.yaml")
    if not os.path.exists(skills_yaml):
        check("skills.yaml exists", FAIL, f"Missing: {skills_yaml}")
    else:
        check("skills.yaml exists", PASS)
        skills_data = load_yaml(skills_yaml)
        skill_ids = set()
        for skill in skills_data.get("skills", []):
            sid = skill.get("id", "<no-id>")
            path = skill.get("path", "")
            abs_path = os.path.join(root, path)
            if sid in skill_ids:
                check(f"Skill id unique: {sid}", FAIL, "Duplicate skill id")
            skill_ids.add(sid)
            if path:
                check(f"Skill file exists: {path}", PASS if os.path.exists(abs_path) else FAIL,
                      f"Missing: {abs_path}" if not os.path.exists(abs_path) else "")
            else:
                check(f"Skill has path: {sid}", FAIL, "No path field")

    # -------------------------------------------------------------------------
    # 4. Command registry vs. filesystem
    # -------------------------------------------------------------------------
    print("\n# 4. Command registry checks")
    commands_yaml = os.path.join(root, ".factory/registry/commands.yaml")
    if not os.path.exists(commands_yaml):
        check("commands.yaml exists", FAIL, f"Missing: {commands_yaml}")
    else:
        check("commands.yaml exists", PASS)
        commands_data = load_yaml(commands_yaml)
        cmd_ids = set()
        for cmd in commands_data.get("commands", []):
            cid = cmd.get("id", "<no-id>")
            src = cmd.get("source", "")
            abs_src = os.path.join(root, src)
            if cid in cmd_ids:
                check(f"Command id unique: {cid}", FAIL, "Duplicate command id")
            cmd_ids.add(cid)
            if src:
                check(f"Command file exists: {src}", PASS if os.path.exists(abs_src) else FAIL,
                      f"Missing: {abs_src}" if not os.path.exists(abs_src) else "")
            else:
                check(f"Command has source: {cid}", FAIL, "No source field")

    # -------------------------------------------------------------------------
    # 5. Skill frontmatter validation
    # -------------------------------------------------------------------------
    print("\n# 5. Skill frontmatter checks")
    skills_root = os.path.join(root, ".agents/skills")
    if not os.path.isdir(skills_root):
        check("Skills root exists", FAIL, f"Missing directory: {skills_root}")
    else:
        check("Skills root exists", PASS)
        for skill_dir in sorted(os.listdir(skills_root)):
            skill_path = os.path.join(skills_root, skill_dir)
            if not os.path.isdir(skill_path):
                continue
            skill_md = os.path.join(skill_path, "SKILL.md")
            rel = os.path.relpath(skill_md, root)
            if not os.path.exists(skill_md):
                check(f"SKILL.md present: {skill_dir}", FAIL, f"Missing: {rel}")
                continue
            with open(skill_md) as f:
                content = f.read()
            if not content.startswith("---"):
                check(f"SKILL.md frontmatter: {skill_dir}", FAIL, "No YAML frontmatter block")
                continue
            parts = content.split("---", 2)
            if len(parts) < 3:
                check(f"SKILL.md frontmatter: {skill_dir}", FAIL, "Malformed frontmatter (no closing ---)")
                continue
            try:
                fm = yaml.safe_load(parts[1])
            except Exception as e:
                check(f"SKILL.md frontmatter: {skill_dir}", FAIL, f"YAML parse error: {e}")
                continue
            if not fm or not fm.get("name"):
                check(f"SKILL.md name field: {skill_dir}", FAIL, "Missing or empty 'name' in frontmatter")
            elif not fm.get("description"):
                check(f"SKILL.md description field: {skill_dir}", FAIL, "Missing or empty 'description' in frontmatter")
            else:
                check(f"SKILL.md frontmatter: {skill_dir}", PASS)
                # Check name matches directory
                if fm["name"] != skill_dir:
                    check(f"SKILL.md name matches dir: {skill_dir}", FAIL,
                          f"frontmatter name='{fm['name']}' does not match directory='{skill_dir}'")
                else:
                    check(f"SKILL.md name matches dir: {skill_dir}", PASS)

    # -------------------------------------------------------------------------
    # 6. Schema file checks
    # -------------------------------------------------------------------------
    print("\n# 6. Schema file checks")
    schemas = [
        ".factory/schemas/finding.schema.json",
        ".factory/schemas/handoff.schema.json",
    ]
    for s in schemas:
        abs_s = os.path.join(root, s)
        if not os.path.exists(abs_s):
            check(f"Schema exists: {s}", FAIL, f"Missing: {abs_s}")
        else:
            try:
                data = load_json(abs_s)
                if "$schema" not in data and "$id" not in data:
                    check(f"Schema valid JSON Schema: {s}", FAIL, "Missing $schema or $id field")
                else:
                    check(f"Schema exists and parses: {s}", PASS)
            except Exception as e:
                check(f"Schema parses: {s}", FAIL, str(e))

    # -------------------------------------------------------------------------
    # 7. Workflow router reference
    # -------------------------------------------------------------------------
    print("\n# 7. Workflow router reference check")
    router_path = os.path.join(root, ".agents/skills/prod-sdlc-factory/references/workflow-router.md")
    check("Workflow router reference exists",
          PASS if os.path.exists(router_path) else FAIL,
          f"Missing: {router_path}" if not os.path.exists(router_path) else "")

    # -------------------------------------------------------------------------
    # 8. Lifecycle YAML state and transition consistency
    # -------------------------------------------------------------------------
    print("\n# 8. Lifecycle state/transition consistency")
    lifecycle_yaml = os.path.join(root, ".factory/workflows/lifecycle.yaml")
    if not os.path.exists(lifecycle_yaml):
        check("lifecycle.yaml exists", FAIL, f"Missing: {lifecycle_yaml}")
    else:
        check("lifecycle.yaml exists", PASS)
        lc = load_yaml(lifecycle_yaml)
        valid_states = set(lc.get("states", []))
        routing = lc.get("routing", [])
        transition_errors = []
        for t in routing:
            frm = t.get("from", "")
            to = t.get("to", "")
            if frm not in valid_states:
                transition_errors.append(f"  from state not in states list: '{frm}'")
            if to not in valid_states:
                transition_errors.append(f"  to state not in states list: '{to}'")
        check("Lifecycle transitions reference valid states",
              FAIL if transition_errors else PASS,
              "\n".join(transition_errors))

    # -------------------------------------------------------------------------
    # 9. Checkpoint template is valid JSON with required fields
    # -------------------------------------------------------------------------
    print("\n# 9. Checkpoint template check")
    checkpoint_path = os.path.join(root, ".factory/templates/checkpoint-template.json")
    if not os.path.exists(checkpoint_path):
        check("checkpoint-template.json exists", FAIL, f"Missing: {checkpoint_path}")
    else:
        try:
            cp = load_json(checkpoint_path)
            required_fields = ["schema_version", "stage", "task_status", "approved_artifacts",
                                "completed_substeps", "pending_substeps", "blockers", "next_action"]
            missing = [f for f in required_fields if f not in cp]
            if missing:
                check("Checkpoint template has required fields", FAIL, f"Missing fields: {missing}")
            else:
                check("Checkpoint template valid", PASS)
        except Exception as e:
            check("Checkpoint template parses", FAIL, str(e))

    # -------------------------------------------------------------------------
    # 10. Capabilities registry available entries resolve to existing paths
    # -------------------------------------------------------------------------
    print("\n# 10. Capabilities registry: available entries resolve")
    cap_yaml = os.path.join(root, "capabilities/registry.yaml")
    if not os.path.exists(cap_yaml):
        check("capabilities/registry.yaml exists", FAIL, f"Missing: {cap_yaml}")
    else:
        check("capabilities/registry.yaml exists", PASS)
        cap = load_yaml(cap_yaml)
        caps_section = cap.get("capabilities", {})
        missing_caps = []
        for category, items in caps_section.items():
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                if item.get("status") != "available":
                    continue
                path = item.get("path") or item.get("source")
                if path:
                    abs_p = os.path.join(root, path)
                    if not os.path.exists(abs_p):
                        missing_caps.append(f"{category}/{item.get('name', '?')}: {path}")
        check("Capabilities registry: available paths exist",
              FAIL if missing_caps else PASS,
              "\n".join(missing_caps))

    # -------------------------------------------------------------------------
    # 11. Handoff template has required sections
    # -------------------------------------------------------------------------
    print("\n# 11. Handoff template check")
    handoff_path = os.path.join(root, ".factory/templates/handoff-template.md")
    if not os.path.exists(handoff_path):
        check("handoff-template.md exists", FAIL, f"Missing: {handoff_path}")
    else:
        with open(handoff_path) as f:
            content = f.read()
        required_sections = ["Work performed", "Files changed", "Acceptance criteria", "Verification evidence",
                              "Blockers", "Next action"]
        missing = [s for s in required_sections if s.lower() not in content.lower()]
        check("Handoff template has required sections",
              FAIL if missing else PASS,
              f"Missing sections: {missing}" if missing else "")

    # -------------------------------------------------------------------------
    # 12. Approval gates policy check
    # -------------------------------------------------------------------------
    print("\n# 12. Approval gates policy check")
    gates_yaml = os.path.join(root, ".factory/policies/approval-gates.yaml")
    if not os.path.exists(gates_yaml):
        check("approval-gates.yaml exists", FAIL)
    else:
        gates = load_yaml(gates_yaml)
        required_gates = ["GATE-SPECS", "GATE-STACK", "GATE-PLAN", "GATE-REVIEW-FIX",
                          "GATE-DESTRUCTIVE", "GATE-GITHUB-WRITE", "GATE-DEPLOY"]
        gates_defined = set(gates.get("gates", {}).keys())
        missing_gates = [g for g in required_gates if g not in gates_defined]
        check("Required approval gates defined",
              FAIL if missing_gates else PASS,
              f"Missing gates: {missing_gates}" if missing_gates else "")

    # -------------------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------------------
    print("\n" + "=" * 50)
    total = len(results)
    passed = sum(1 for r in results if r["status"] == PASS)
    failed = sum(1 for r in results if r["status"] == FAIL)
    blocked = sum(1 for r in results if r["status"] == BLOCKED)

    print(f"Total: {total}  Passed: {passed}  Failed: {failed}  Blocked: {blocked}")
    print("=" * 50 + "\n")

    if failed > 0:
        print("VALIDATION FAILED — fix the issues above before marking the factory complete.")
        return 1
    if blocked > 0:
        print("VALIDATION PARTIAL — blocked checks require external resources or credentials.")
        return 0
    print("VALIDATION PASSED — all structural checks succeeded.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="prod-sdlc-factory validation suite")
    parser.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        help="Repository root directory (default: parent of tests/)")
    args = parser.parse_args()
    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"ERROR: Repository root does not exist: {root}")
        sys.exit(1)
    print(f"Repository root: {root}")
    sys.exit(run_all(root))


if __name__ == "__main__":
    main()

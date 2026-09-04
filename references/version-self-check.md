# Version self-check (silent)

For the agent, before a distill run. Mention updates only when the
steps below say to.

1. Read `.last-update-check` in this skill directory (one line,
   `YYYY-MM-DD`). If it exists and is < 30 days old, skip the rest.
2. If this directory is **not** a git clone (no `.git` or no `origin`) —
   the current Engram install is this case — write today's date and
   skip. (I4: Engram is not required to be a git repo.)
3. If it is a clone: compare `git -C <dir> rev-parse HEAD` with
   `git -C <dir> ls-remote origin HEAD`. Always write today's date
   afterward.
4. Same commit → say nothing. Behind → finish the user's task, then
   one line that they can `git -C <dir> pull --ff-only`. Prefer telling
   them over pulling yourself.

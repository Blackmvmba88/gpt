# GPT Repository Instructions

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Repository Overview
This is a minimal GPT-related repository that currently contains only basic documentation. The repository is in an early development stage with no established build system, dependencies, or runnable code.

## Working Effectively

### Initial Setup
- Clone the repository: `git clone [repository-url]`
- Navigate to repository: `cd gpt`
- Check repository status: `git --no-pager status`

### Current Repository State
- **No build system**: There are no package.json, requirements.txt, Makefile, or other build configuration files
- **No dependencies**: No dependency management system is currently in place
- **No tests**: No test framework or test files exist
- **No CI/CD**: No GitHub Actions workflows are configured

### Validation Commands
Since this repository has no build system, traditional build and test validation is not applicable. Instead, validate basic repository operations:

1. **Repository integrity check**: `git --no-pager log --oneline -5`
2. **File listing**: `ls -la`
3. **Content verification**: `cat README.md`

These commands complete in under 1 second each.

## Development Guidelines

### Before Making Changes
- Always check current repository state: `git --no-pager status`
- Review existing files: `ls -la`
- Check commit history: `git --no-pager log --oneline -10`

### When Adding New Features
Since this repository lacks infrastructure, when adding new functionality:

1. **Determine technology stack** based on the intended purpose (Python, Node.js, Go, etc.)
2. **Initialize appropriate build system**:
   - For Node.js: `npm init -y`
   - For Python: Create `requirements.txt` and `setup.py`
   - For Go: `go mod init github.com/Blackmvmba88/gpt`
3. **Add development dependencies** and configure build/test commands
4. **Update these instructions** with validated build and test procedures

### Commit Guidelines
- Always check what you're committing: `git --no-pager diff --cached`
- Use descriptive commit messages
- Push changes: `git push origin [branch-name]`

## Common Tasks

### Repository Structure
```
.
├── .git/               # Git metadata
├── .github/           # GitHub configuration (created for Copilot instructions)
│   └── copilot-instructions.md
└── README.md          # Basic repository documentation
```

### README.md Content
```
# gpt
jiji
```

### Git Operations
- **Check status**: `git --no-pager status` (< 1 second)
- **View history**: `git --no-pager log --oneline -10` (< 1 second)
- **Create branch**: `git checkout -b feature/new-feature` (< 1 second)
- **Add files**: `git add .` (< 1 second)
- **Commit changes**: `git commit -m "Description"` (< 1 second)
- **Push changes**: `git push origin [branch]` (< 5 seconds, depends on network)

## Future Development Setup

When this repository evolves to include actual code, update this section with:

### For Python Projects
- **Setup**: `python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
- **Build**: Document specific build commands when implemented
- **Test**: `python -m pytest` (timing TBD based on test suite)
- **Run**: Document application startup commands

### For Node.js Projects
- **Setup**: `npm install` (timing depends on dependencies)
- **Build**: `npm run build` (timing TBD - NEVER CANCEL, set timeout 60+ minutes)
- **Test**: `npm test` (timing TBD - NEVER CANCEL, set timeout 30+ minutes)
- **Run**: `npm start` or `npm run dev`

### For Go Projects
- **Setup**: `go mod download` (timing depends on dependencies)
- **Build**: `go build ./...` (timing TBD)
- **Test**: `go test ./...` (timing TBD)
- **Run**: `go run main.go` or `./[binary-name]`

## Validation Scenarios

### Current Validation (Empty Repository)
Since no application logic exists, validation consists of:
1. **Repository accessibility**: Can clone and navigate the repository
2. **Git operations**: Can view history, create branches, commit changes
3. **File integrity**: README.md exists and contains expected content

### Future Validation Scenarios
When application code is added, always test:
1. **Installation process**: Fresh clone → dependencies → build → run
2. **Core functionality**: Exercise primary use cases of the application
3. **Error handling**: Test with invalid inputs or edge cases
4. **Documentation accuracy**: Verify all commands in instructions work correctly

## Critical Reminders

- **NEVER CANCEL** long-running builds or tests when they are implemented
- Always set appropriate timeouts (60+ minutes for builds, 30+ minutes for tests)
- Validate every command before documenting it in instructions
- Test complete user scenarios, not just technical operations
- Update these instructions when the repository evolves

## Notes for Future Contributors

This repository is currently a blank slate. The first major contribution should:
1. Define the project's purpose and scope
2. Choose appropriate technology stack
3. Implement basic project structure
4. Add build/test infrastructure
5. Update these instructions with validated procedures

When implementing GPT-related functionality, consider:
- Model integration requirements
- API design and authentication
- Performance and scalability needs
- Testing strategies for AI/ML components
- Documentation for model usage and limitations
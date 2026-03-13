# 🔒 Security Policy

## Reporting Vulnerabilities

If you discover a security vulnerability in Brainrot, please **do NOT open a public GitHub issue**. Instead:

1. **Email:** security@brainrot.internal
2. **Include:**
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if applicable)

3. **Timeline:**
   - We aim to respond within 48 hours
   - We will work with you to verify and fix the issue
   - Public disclosure will be coordinated

## Security Best Practices for Contributors

### Code Review
- All code changes go through peer review
- Security implications should be explicitly discussed
- Tests must be included for security-related changes

### Dependencies
- Keep dependencies up to date
- Report deprecated/vulnerable packages immediately
- Use `npm audit` before committing

### Data Handling
- All user data is stored locally in browser (localStorage)
- No data is sent to external servers
- Entertainment/educational content only - no sensitive information

### ASMR Audio Synthesis
- Web Audio API is used for real-time synthesis
- No external audio files or APIs required
- No audio is recorded or stored

### JSON Configuration Files
- Configuration files contain no sensitive data
- All JSON files are treated as public documentation
- No API keys or credentials should ever be committed

## Security Headers Recommendation

If deploying to production, implement:
```
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
```

## Known Limitations

1. **No HTTPS Enforcement** - This is a local-first application
2. **No Authentication** - Age gate is client-side only
3. **No Input Validation** - All data comes from trusted JSON files
4. **No Rate Limiting** - This is not a backend service

## Security Testing

- Regular dependency audits via GitHub Actions
- Manual security review before major releases
- Community security disclosure program

## Credits

We appreciate responsible security researchers. Acknowledged contributors to security will be listed (with permission) in our Hall of Fame.

---

**Last Updated:** 2026-03-13
**Maintained by:** Brainrot Platform | Terminal-First Development

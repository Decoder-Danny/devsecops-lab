# DevSecOps Home Lab

A production-grade DevSecOps pipeline demonstrating secure software delivery
practices aligned with DoD IL2/IL4 environments.

## Architecture
- **Runtime**: k3s (via k3d) on local Kubernetes
- **CI/CD**: GitHub Actions with integrated security gates
- **IaC**: Terraform + Checkov policy scanning
- **Container Security**: Trivy image scanning + Kyverno admission policies
- **Runtime Security**: Falco threat detection
- **Secrets**: HashiCorp Vault
- **Compliance**: OpenSCAP/InSpec STIG-aligned profiles (Continuous ATO simulation)

## Security Gates in Pipeline
1. Secret scanning (Gitleaks)
2. SAST (Semgrep)
3. Container image scanning (Trivy)
4. IaC scanning (Checkov)
5. Kubernetes policy enforcement (Kyverno)

## Compliance
Automated NIST 800-53 control validation mapped to DISA STIG benchmarks.

## Docs
- [Architecture Diagram](docs/diagrams/architecture.md)
- [Network Diagram](docs/diagrams/network.md)
- [Demo Script](docs/DEMO.md)
EOF

#!/bin/bash

# Generate Terraform infrastructure diagram
# Requires: graphviz (brew install graphviz)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
TERRAFORM_DIR="$PROJECT_ROOT/infrastructure/terraform/environments/prod"
OUTPUT_DIR="$PROJECT_ROOT/docs/architecture"

echo "🎨 Generating Terraform infrastructure diagram..."

# Check if graphviz is installed
if ! command -v dot &> /dev/null; then
    echo "❌ Error: graphviz not installed"
    echo "Install with: brew install graphviz"
    exit 1
fi

# Check if terraform directory exists
if [ ! -d "$TERRAFORM_DIR" ]; then
    echo "❌ Error: Terraform directory not found: $TERRAFORM_DIR"
    exit 1
fi

# Navigate to terraform directory
cd "$TERRAFORM_DIR"

# Initialize if needed
if [ ! -d ".terraform" ]; then
    echo "📦 Initializing Terraform..."
    terraform init -backend=false
fi

# Generate graph
echo "📊 Generating graph..."
terraform graph | dot -Tpng -Gdpi=300 > "$OUTPUT_DIR/terraform-graph.png"

echo "✅ Diagram generated: $OUTPUT_DIR/terraform-graph.png"
echo "📏 Size: $(du -h "$OUTPUT_DIR/terraform-graph.png" | cut -f1)"

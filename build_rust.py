import os
import shutil
import subprocess

print("Cleaning previous build artifacts...")

if os.path.exists("src-rust/generated"):
    shutil.rmtree("src-rust/generated")

if os.path.exists("src-rust/target"):
    shutil.rmtree("src-rust/target")

print("Building Rust helpers...")

subprocess.run(
    ["cargo", "build", "--release"],
    cwd="src-rust",
)

print("Generating C headers for Rust API...")

subprocess.run(
    [
        "cbindgen",
        "--config",
        "cbindgen.toml",
        "--crate",
        "rusthelpers",
        "--output",
        "generated/rusthelpers.h",
        "--cpp-compat",
    ],
    cwd="src-rust",
)

print("Successfully built Rust helper API")

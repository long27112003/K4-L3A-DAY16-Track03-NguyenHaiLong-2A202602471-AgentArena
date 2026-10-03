import os
import zipfile

def create_harness_zip(output_path="harness_2A202602471.zip", source_dir="harness"):
    # Create zip file with harness folder and its contents
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_dir):
            # Exclude __pycache__
            if "__pycache__" in root:
                continue
            for file in files:
                if file.endswith((".pyc", ".pyo")):
                    continue
                file_path = os.path.join(root, file)
                # Archive name preserves 'harness/...' path
                arcname = os.path.relpath(file_path, os.path.dirname(source_dir))
                zf.write(file_path, arcname)
                print(f"Added: {arcname}")
    print(f"\nSuccessfully created {output_path} (size: {os.path.getsize(output_path)} bytes)")

if __name__ == "__main__":
    create_harness_zip()

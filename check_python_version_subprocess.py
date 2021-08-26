import subprocess

#ejecutar con python3.9
process = subprocess.run(['which', 'python3'], capture_output=True)
print(process)

if process.returncode != 0:
    raise OSError('Sorry python3 is not installed')

python_bin = process.stdout.strip()

print(f'Python found in: {python_bin}')

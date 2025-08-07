import subprocess

def get_cpu_id():
    command = 'Get-CimInstance -ClassName Win32_Processor | Select-Object -ExpandProperty ProcessorId'
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == "__main__":
    cpu_id = get_cpu_id()
    print(f"CPU ID: {cpu_id}")

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import subprocess

def index(response):
    return HttpResponse("ths is homepage")

def run_command(command):
    """
    Executes a given command and returns the output or error.
    :param command: The command to execute.
    :return: Output of the command.
    """
    try:
        # Run the command
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.stdout:
            return result.stdout.strip()
        elif result.stderr:
            return f"Error: {result.stderr.strip()}"
        else:
            return "No output"
    except Exception as e:
        return f"Exception occurred: {str(e)}"

def system_info(request):
    """
    Django view to execute system commands and return their output as a JSON response.
    """
    # Commands to execute
    commands = {
        "OS Name, Version, Architecture": "wmic os get Caption, Version, OSArchitecture",
        "Build Number": "wmic os get BuildNumber",
        "Kernel Version": "wmic os get Version",
        "Processor Usage": "wmic cpu get LoadPercentage",
        "Memory Usage": "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize",
        "Swap Memory Usage": "wmic OS get FreeVirtualMemory,TotalVirtualMemorySize",
        "IP Address": "ipconfig",
    }

    # Execute commands and collect results
    results = {}
    for description, command in commands.items():
        results[description] = run_command(command)

    # Return results as a JSON response
    return JsonResponse(results)

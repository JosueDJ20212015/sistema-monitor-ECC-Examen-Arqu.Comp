import psutil
import platform
import time
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'sistema/index.html')

def system_data(request):
    try:
        # CPU
        cpu_percent = psutil.cpu_percent(interval=0.5)
        cpu_freq = psutil.cpu_freq()
        cpu_model = platform.processor() or "Procesador desconocido"
        
        # Memoria
        memory = psutil.virtual_memory()
        
        # Disco
        disk = psutil.disk_usage('/')
        disk_type = "SSD"
        
        # Red
        net = psutil.net_io_counters()
        
        # Temperatura CPU
        temps = psutil.sensors_temperatures() if hasattr(psutil, "sensors_temperatures") else {}
        cpu_temp = None
        if temps:
            for name, entries in temps.items():
                if entries:
                    cpu_temp = entries[0].current
                    break
        
        # sistema - Uptime
        boot_time = psutil.boot_time()
        uptime_seconds = time.time() - boot_time
        uptime_hours = int(uptime_seconds // 3600)
        uptime_minutes = int((uptime_seconds % 3600) // 60)
        
        # informacion requerida
        data = {
            # CPU
            "cpu": cpu_percent,
            "cores": psutil.cpu_count(logical=True),
            "cpu_model": cpu_model,
            "cpu_freq_current": round(cpu_freq.current / 1000, 2) if cpu_freq else 0,
            "cpu_freq_max": round(cpu_freq.max / 1000, 2) if cpu_freq else 0,
            
            # memoria
            "memory_used": round(memory.used / (1024 ** 3), 2),
            "memory_total": round(memory.total / (1024 ** 3), 2),
            "memory_percent": memory.percent,
            "memory_type": "DDR4",
            "memory_speed": "3200",
            
            # disco
            "disk_used": round(disk.used / (1024 ** 3), 2),
            "disk_total": round(disk.total / (1024 ** 3), 2),
            "disk_percent": disk.percent,
            "disk_type": disk_type,
            "disk_model": "Unidad Principal",
            
            # Red
            "net_sent": round(net.bytes_sent / (1024 ** 2), 2),
            "net_recv": round(net.bytes_recv / (1024 ** 2), 2),
            
            # Temperatura
            "cpu_temp": cpu_temp,
            
            # Sistema
            "system": f"{platform.system()} {platform.release()}",
            "system_version": platform.version(),
            "uptime": f"{uptime_hours}h {uptime_minutes}m",
            "processes": len(psutil.pids()),
        }
        
        return JsonResponse(data)
        
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
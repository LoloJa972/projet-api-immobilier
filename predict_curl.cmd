@echo off
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"superficie\": 100, \"nombre_pieces\": 4, \"distance_centre\": 2}"
pause
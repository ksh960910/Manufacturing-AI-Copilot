from app.vision.detector import detect_objects

image_path = 'data/raw/pcb/test/images/01_mouse_bite_13_jpg.rf.8f521857c9486ccdf7ba631d6ccf39c6.jpg'

results = detect_objects(image_path)

print('='*50)
print('Detection Results')
print('='*50)

for result in results:
    print(result)





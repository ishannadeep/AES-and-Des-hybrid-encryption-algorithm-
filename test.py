import aes_2
import time
import base64

with open("girl.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
   
start_time = time.time()
encry=aes_2.encrypt('ahdfsujeytsbsdfawskdfhsdgfereijd', my_string)
print("time for encryption --- %s seconds ---" % (time.time() - start_time))
with open("encry_test_Img.enc", "wb") as img_file:
    img_file.write(encry)

start_time2 = time.time()
decry=aes_2.decrypt('ahdfsujeytsbsdfawskdfhsdgfereijd',encry)
print("time for decryption --- %s seconds ---" % (time.time() - start_time2))
with open("out_test_Img.jpeg", "wb") as img_file:
    img_file.write(base64.b64decode(decry))

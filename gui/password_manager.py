from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    
    #creating key
    def create_key(self, path):
        self.key = Fernet.generate_key()

        with open(path, 'wb') as file:
            file.write(self.key)

    #getting/loading the (same) key that would be used for decryption
    def load_key(self, path):
        with open(path, 'rb') as file:
            self.key = file.read().strip()

    #creates a new file to store the passwords
    def create_password_file(self, path, initial_values = None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key,value)
    
    #loads the file that already has the passwords
    def load_password_file(self,path):
        self.password_file = path

        with open(path, 'r') as file:
            for line in file:
                site, encrypted = line.split('|')
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    #adds and ecrypts a new password
    def add_password(self,site,password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file,'a') as file:
                encrypted = Fernet(self.key).encrypt(password.encode())
                file.write(site+'|'+encrypted.decode()+'\n')

    #well... gets the password... idk how to say it any other way....
    def get_password(self,site):
        return self.password_dict[site]
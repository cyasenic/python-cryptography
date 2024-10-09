#This is same file as the hashing.py but with salted hashes as a way to get more secure hashes
#library for hashing text values or data
import hashlib
import argparse

#supported hashing algorithms
hashing_algorithms = ["MD5","SHA256", "SHA512", "md5", "sha256", "sha512"]

#function for receiving hashing parameters
def hash(hash_algorithm, salt, data):
    try:
        
        if hash_algorithm not in hashing_algorithms:
            return "Algroithm not supported!"
        
        if hash_algorithm == "MD5" or hash_algorithm == "md5":
            try:
                md5_hash = hashlib.md5(salt.encode("utf-8") + data.encode("utf-8")).hexdigest()
                return md5_hash
            except Exception as md5_error:
                print(md5_error)
                    
        if hash_algorithm == "SHA256" or hash_algorithm == "sha256":
            try:
                sha256_hash = hashlib.sha256(salt.encode("utf-8") + data.encode("utf-8")).hexdigest()
                return sha256_hash
            except Exception as sha_256_error:
                return sha_256_error
            
        if hash_algorithm == "SHA512" or hash_algorithm == "sha512":
            try:
                sha512_hash = hashlib.sha512(salt.encode("utf-8") + data.encode("utf-8")).hexdigest()
                return sha512_hash
            except Exception as sha512_error:
                return sha512_error
                    
    except Exception as hashing_error:
        return hashing_error

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hashing strings with different hashing algorithims")
    parser.add_argument("--algorithm", dest="algo", action="store", required=True, type=str)
    parser.add_argument("--data", dest="data", action="store", required=True, type=str)
    parser.add_argument("--salt", dest="salt", action="store", required=True, type=str)
    
    arguments = parser.parse_args()
    
    hashed_data = hash(arguments.algo, arguments.salt, arguments.data)
    print(hashed_data)

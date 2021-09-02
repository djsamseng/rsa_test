import rsa

def bytes_to_int(raw_bytes):
    return int.from_bytes(raw_bytes, "big", signed=False)

def encrypt_int(message, e, n):
    return pow(message, e, n)

def main():
    # openssl rsa -in private.pem -noout -text
    # should give RSA Private-Key: (512 bit, 2 primes)
    pub, priv = rsa.newkeys(512)
    message = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA".encode()

    # copy from output of ./gen_keys.sh
    pub_n = 9432073003817491131991824661655029166535242011361962822995316772710222235701333912590952492348967268308549211947062848480630804541764641799735292463131139 #pub.n
    # copy from output of ./gen_keys.sh
    pub_e = 65537 # pub.e

    padded = message
    payload = bytes_to_int(padded)
    encrypted = encrypt_int(payload, pub_e, pub_n)
    print(encrypted)
    # Should match
    # openssl rsautl -encrypt -inkey public.pem -pubin -in message.txt -raw -hexdump

if __name__ == "__main__":
    main()
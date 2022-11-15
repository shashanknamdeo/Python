def generateTOTP(username):
    """
    """
    import os
    import pyotp
    from GlobalVariables import KITECONNECT_DATA_DIR
    with open(os.path.join(KITECONNECT_DATA_DIR, 'Security', 'TOTP_'+str(username)+'.txt')) as secretkey_file:
        totp_secret_key = secretkey_file.readline()
    # 
    totp= pyotp.TOTP('ROHOBQKIHWAT23UFAXGV5HEEGKLZN6P4')
    totp_pin = totp.now()
    return totp_pin
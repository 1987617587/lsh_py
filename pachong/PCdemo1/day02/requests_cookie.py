import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Cooike" : "RK=yhxh8l7Xdi; ptcz=4841263a59910979c6928ec7bf6aeba954f59f5b3e43064d1fa1bfe4d66d8c7f; pgv_pvid=7478598780; qm_logintype=qq; edition=mail.qq.com; webp=1; pgv_pvi=8346832896; eas_sid=L185Z8843570r4u8w1w3v2n807; o_cookie=1987617587; pac_uid=1_1987617587; ptui_loginuin=1711960368; lskey=0001000023f0c1c9b51ff24d8a89f474c4f7be6a1e775973e0001df82716fba0385eb42ba5ad6d40e834364f; p_uin=o1987617587; wimrefreshrun=0&; qm_antisky=1987617587&0d271338d2cab704a0dd6714abe0ef77f388e0f7ae795eaf47a5295a477cb52d; qm_flag=0; qqmail_alias=18336068360@qq.com; new_mail_num=1987617587&0; qm_domain=https://mail.qq.com; foxacc=1987617587&0; pgv_si=s4908132352; uin=o1987617587; skey=@YSmyhuKLc; pt4_token=FRJYD3rYIcmLyPljmOA6wKPf7wtLsS0*IPOR0FY4ICE_; p_skey=wUtbEt8vF*PepsXVPEwbrJ9Vb12JdAbBW-yc826usa0_; sid=1987617587&acbb74965c167f2ae51597972b060cf1,qd1V0YkV0OHZGKlBlcHNYVlBFd2JySjlWYjEySmRBYkJXLXljODI2dXNhMF8.; qm_username=1987617587; qm_lg=qm_lg; qm_ptsk=1987617587&@YSmyhuKLc; ssl_edition=sail.qq.com; qm_loginfrom=1987617587&wpt; username=1987617587&1987617587; CCSHOW=000000"
}


url = "https://mail.qq.com/cgi-bin/frame_html?sid=MgG5cNNjtc20bRtF&r=04777a38c0fd0bc1c3d9ce8363c3dcfd"
response = requests.get(url, headers=headers)
print(response.text)
print(response.url)
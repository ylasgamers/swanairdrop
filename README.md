# Airdrop Swan Chain Helper Claim
# Usage : [Make Sure Already Install Python 3.10 & Requirements Below Before Run/Use!!!]
```
python airdropswanclaim.py or python3 airdropswanclaim.py
```
- Recomended Using Python 3.10
- For Windows [Download Here](https://www.python.org/downloads/release/python-3100/) [Scrool Down]
- Maybe For Windows 10 Or Higher You Can Install Python 3.10 From Microsoft Store
```
- Install Requirements
python -m pip install pip --upgrade
pip install requests
pip install web3==6.20.1
```
- For Termux Android [Download Here](https://f-droid.org/repo/com.termux_1020.apk) [F-Droid Version]
```
After Install Termux, Make Sure Allowed Permission Storage On Setting Termux
- Install Python 3.10
pkg update && upgrade
pkg install tur-repo
pkg install python-is-python3.10
- Install Requirements
pip install --upgrade pip
pkg install -y rust binutils
CARGO_BUILD_TARGET="$(rustc -Vv | grep "host" | awk '{print $2}')" pip install maturin
pip install requests
pip install web3==6.20.1
```
- For Ubuntu 18.04 | 20.04 | 22.04 (VPS)
```
- Install Python 3.10
apt update && sudo apt upgrade -y
apt install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa
apt install python3.10
apt install python3-pip
- Install Requirements
pip install requests
pip install web3==6.20.1
```

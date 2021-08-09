# Homework Wallet




```bash
$ pip install -r requirements.txt
```
```bash
>>> from wallet import *
```
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_derive.png)
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_derive.png)


### Getting Account Access (BTCTEST, and ETH) using private Key
```bash
>>> Account_ETH = priv_key_to_account(ETH, (coins[ETH][0]['privkey']))
>>> Account_BTCTEST = priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey']))
```
## Account that will Receive BTCTEST
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_address.png)


## Send BTCTEST Formula
```bash
>>> send_tx(BTCTEST, Account_BTCTEST, 'n3xdmfgWz8ZvMnqPYxoDS8rtfARNJtDBE2', 0.0000001)
>>> print(priv_key_to_account(BTCTEST, (coins[BTCTEST][0]['privkey'])).get_transactions()[0])
5b37c293e2322f68a0786b8ec4e6a020bbdc061a12a300b6fb3c787ca60c69f1
```

## Confirm BTCTEST transmission on https://tbtc.bitaps.com/
![image](https://github.com/abacella/wallet/blob/main/Screenshots/btc_block.png)


## Account that will Receive ETH
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_address.png)

## Send ETH Formula
```bash
>>> send_tx(ETH, Account_ETH, '0xCE4B45cD08Dd665900a70282f0714560Bc8AE38C', 1000)
HexBytes('0x8dac21294a03ff81ed5900af9212a232a658f56f2ee8b9319915434e997378bc')
```

## Confirm ETH transaction on MyCrypto
![image](https://github.com/abacella/wallet/blob/main/Screenshots/eth_mycrypto.png)


## How to install HD-Wallet-Derive
Tutorial from https://columbia.bootcampcontent.com/columbia-bootcamp/cu-nyc-virt-fin-pt-03-2021-u-c/-/blob/master/02-Homework/19-Blockchain-Python/Instructions/Resources/HD_Wallet_Derive_Install_Guide.md

# HD-Wallet-Derive Install Guide

This guide serves as a step by step process for setting up the [`hd-wallet-derive` library](https://github.com/dan-da/hd-wallet-derive) used to derive `BIP32` addresses and private keys for Bitcoin and other alternative coins or "altcoins."

If you need additional help in the installation process, you can follow the step by step video guides in the following links.

<details><summary>Microsoft Windows Users</summary>

* [Installing PHP Version 7.3 for Windows](https://youtu.be/IvcZZaIEL_4)

* [HD Derive Wallet Install for Windows](https://youtu.be/A_tqm4j4vsY)

</details>

<details><summary>macOS Users</summary>

* [Installing PHP Using the Homebrew Package Manger for Mac](https://youtu.be/SNRQSwlOKbs)

* [HD Derive Wallet Install for Mac](https://youtu.be/c-Qc3Pss6oM)

</details>

## Step 1 - Environment Setup

The `hd-wallet-derive` library is written in the PHP language; therefore, you will be required to first set up PHP on your machines before installing and then running the `hd-wallet-derive` library.



<details><summary>Environment Setup in macOS Operating System</summary>

For those using **macOS**, execute the following steps:

1. macOS users will need to update their machine's prebuilt version of PHP to the full version using a package manager for macOS called Homebrew.

2. To do this, visit the [Homebrew website](https://brew.sh/) and install Homebrew using the given install command.
   
   <img alt=homebrew-install src=Images/homebrew-install.png width=700>

3. Once Homebrew is installed, execute the following command in your terminal. This should install the latest version of PHP (7.3 at this current time).

    ```shell
    brew install php@7.3
    ```

4. Next, execute the command appropriate for your system:

    * macOS Catalina and above (`zsh` shell):

      ```shell
      echo "export PATH=/usr/local/opt/php@7.3/bin:$PATH" >> ~/.zshrc
      ```

    * Versions prior to macOS Catalina (`bash` shell):

      ```shell
      echo "export PATH=/usr/local/opt/php@7.3/bin:$PATH" >> ~/.bash_profile
      ```

    * **Note:** If you are on macOS Catalina and up (10.15+), your default shell is now `zsh`, instead of `bash` as in previous versions. No worries, however, since `zsh` can handle the same tasks. If you have yet to upgrade to Catalina, you will be using `bash` as your default shell, which will affect the commands you need to run. Make sure you are running the commands appropriate for your system!  

5. **Close the terminal**. 

6. Open a **NEW** terminal, then verify that PHP version 7.3 is the current version in your system by executing the following command:

    ```shell
    php -version
    ```

7. If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!

   <img alt=PHP-macOS-install-3 src=Images/php-os-x-3.png width=700>

</details>



## Installing hd-wallet-derive 

With the latest version of PHP installed on our machines, we can now proceed to the installation of the `hd-wallet-derive` library.

1. With your terminal open as indicated for your operating system, cd into your `Blockchain-Tools folder and run the following code:

    ```shell
      git clone https://github.com/dan-da/hd-wallet-derive
      cd hd-wallet-derive
      curl https://getcomposer.org/installer -o installer.php
      php installer.php
      php composer.phar install
    ```

3. You should now have a folder called `hd-wallet-derive` containing the PHP library!

## Troubleshooting macOS hd-wallet-derive

If you run into an issue with the installation of `hd-wallet-derive` due to `php extension gmp` missing on macOS installation of PHP, here are the steps to resolve:

1. Run the command `brew unlink php@7.3` this unlinks the current version of PHP running on mac. 

2. Run the command `brew upgrade php@7.3` this will update your current version of PHP to the latest version of `php7.3.x`. 
  - If you receive the message that PHP `7.3.x` version is already installed proceed to the next step.

3. Run the command `brew link php@7.3 --overwrite` this will relink the corresponding path and connect the extensions (including gmp).

4. With your terminal open as indicated for your operating system, cd into your `Blockchain-Tools folder and run the following code:

    ```shell
      git clone https://github.com/dan-da/hd-wallet-derive
      cd hd-wallet-derive
      curl https://getcomposer.org/installer -o installer.php
      php installer.php
      php composer.phar install
    ```

</details>

<details><summary>Verification</summary>

1. Run the command to `cd` in your `hd-wallet-derive` folder.

2. Once you've confirmed your are in your `hd-wallet-derive` folder, execute the following command:

    ```shell
    ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change
    ```

3. If installation was successful, you should see output similar to what you see in the following image:

   <img alt=hd-wallet-derive-execute src=Images/hd-wallet-derive-execute.png width=700>

</details> 
<br>

### Congratulations! The `hd-wallet-derive` library should now be working and good to go!

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.







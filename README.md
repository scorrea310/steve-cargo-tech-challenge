when you're in a long pairing session with a coworker debugging shitty code and you finally git blame showing that it's your coworkers code...

![Alt Text](https://github.com/scorrea310/steve-cargo-tech-challenge/raw/main/no.gif)

# steve-cargo-tech-challenge

## Prerequisites
- have python version 3.3 or later on your computer.
- Have Terraform installed on your computer.
- Have AWS cli on your computer and have configured your aws account with `aws configure`
- git clone this repo with `git clone https://github.com/scorrea310/steve-cargo-tech-challenge.git`  
## problems 1 and 3  
1. Run problems 1 and 3 by cd'ing into the problems-1-and-3 folder.
2. create virtual env using `python3 -m venv .venv`
3. start virtual env using `source .venv/bin/activate`
4. run `pip install -r requirements.txt` and then finally run `python3 1-and-3.py` 

## problem 2
1. cd into problem-2 folder
2. run `terraform init` to initilize terraform and aws provider
3. run `terraform plan` to check you're not going to burn down the world.
4. run `terraform apply` to apply terraform changes. Don't be that dummy senior engineer you told me about.
5. run `terraform destroy` to destroy resources and so that your wallet doesn't get destroyed.

## Things I would do to make my code more production ready:
* For problem 1 and 3, take the code out of the global scope and put it in functions/classes and also add error handling just to name a few.
* For problem 3, I would use a remote backend for hosting my state file using either Terraform cloud, s3, or somewhere else. I would also backup my state file.

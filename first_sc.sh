#! usr/bin/ env bash
#
#SBATCH --job-name=hello
#SBATCH --output=res.txt
#
#SBATCH --ntasks=1
#SBATCH --time=05:00
##SBATCH --mem-per-cpu=200
#SBATCH --patition=a100
#SBATC --cpus-per-task=18

# load the module
#module load example lol

# move to the working directory
# cd ..

# do the submission
python3 demo.py
sleep 60


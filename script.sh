#!/bin/bash
#PBS -N bloom_benchmark
#PBS -l walltime=00:30:00
#PBS -l nodes=1:ppn=1
#PBS -l mem=4gb

cd $PBS_O_WORKDIR

module load Miniconda3
conda activate bloom

python benchmark.py
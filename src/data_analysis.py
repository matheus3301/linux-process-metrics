import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def create_dataset_from_file(filename: str):
    dataset = pd.read_csv(filename)
    # dataset['timestamp'] = pd.to_datetime(dataset['timestamp'])

    return dataset

def show_statistical_information(dataset: pd.DataFrame):
    print(dataset.describe())

def show_plots(dataset: pd.DataFrame):
    fontsize=6

    x = dataset['timestamp']
    mem = dataset['memmory']
    cpu = dataset['cpu']
    write = dataset['write_bytes']
    read = dataset['read_bytes']

    fig, axs = plt.subplots(2,2)

    fig.suptitle('Resource Usage Analasys')

    axs[0,0].plot(x, mem)
    axs[0,0].set_title('Memmory')
    axs[0,0].set_xlabel('Timestamp')
    axs[0,0].set_ylabel('Usage (Bytes)')

    


    axs[0,1].plot(x, cpu)
    axs[0,1].set_title('CPU')
    axs[0,1].set_xlabel('Timestamp')
    axs[0,1].set_ylabel('Usage (%)')
    axs[0,1].set_ylim([0,100])


    
    axs[1,0].plot(x, write)
    axs[1,0].set_title('Write Bytes')
    axs[1,0].set_xlabel('Timestamp')
    axs[1,0].set_ylabel('Usage (Bytes)')


    axs[1,1].plot(x, read)
    axs[1,1].set_title('Read Bytes')
    axs[1,1].set_xlabel('Timestamp')
    axs[1,1].set_ylabel('Usage (Bytes)')

    plt.show()

    
    
    
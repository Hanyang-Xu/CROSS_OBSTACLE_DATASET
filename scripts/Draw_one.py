import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from matplotlib import lines

# Change to the absolute address of the downloaded dataset.
path = "D:\\lab\\Cross_obstacle_data_sets\\CROSS_OBSTACLE_DATASET\\Datasets\\AB07"  # Read one subject at a time.
Cate = ['Left', 'Right']
Height = ['h0', 'h75', 'h150', 'h225', 'h300']  # choose height from ['h0', 'h75', 'h150', 'h225', 'h300']
color_dict = {'h0': 'grey', 'h75': 'orange', 'h150': 'dodgerblue', 'h225': 'lime', 'h300': 'violet'}

fileList = os.listdir(path)
for cate in fileList:
    print(cate)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(3, 3, 1)
    plt.title('Hip joint')
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Hip Angle (deg)')
    ax2 = fig1.add_subplot(3, 3, 2)
    plt.title('Knee joint')
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Knee Angle (deg)')
    ax3 = fig1.add_subplot(3, 3, 3)
    plt.title('Ankle joint')
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ankle Angle (deg)')
    ax4 = fig1.add_subplot(3, 3, 4)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Hip Moment (Nm/Kg)')
    ax5 = fig1.add_subplot(3, 3, 5)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Knee Moment (Nm/Kg)')
    ax6 = fig1.add_subplot(3, 3, 6)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ankle Moment (Nm/Kg)')
    ax7 = fig1.add_subplot(3, 3, 7)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ground Reaction Force (N)')
    ax8 = fig1.add_subplot(3, 3, 8)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ground Reaction Force (N)')
    ax9 = fig1.add_subplot(3, 3, 9)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ground Reaction Force (N)')

    AX = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]

    # Construction legend
    line1 = lines.Line2D([0], [0], label='0cm', lw=2, c='grey')
    line2 = lines.Line2D([0], [0], label='7.5cm', lw=2, c='orange')
    line3 = lines.Line2D([0], [0], label='15cm', lw=2, c='dodgerblue')
    line4 = lines.Line2D([0], [0], label='22.5cm', lw=2, c='lime')
    line5 = lines.Line2D([0], [0], label='30cm', lw=2, c='violet')
    handles = [line1, line2, line3, line4, line5]

    file_path = os.path.join(path, str(cate))

    # get all data with a Dataframe type
    force = pd.read_excel(file_path, sheet_name='force')
    ankle_angle = pd.read_excel(file_path, sheet_name='ankle_angle')
    ankle_moment = pd.read_excel(file_path, sheet_name='ankle_moment')
    knee_angle = pd.read_excel(file_path, sheet_name='knee_angle')
    knee_moment = pd.read_excel(file_path, sheet_name='knee_moment')
    hip_angle = pd.read_excel(file_path, sheet_name='hip_angle')
    hip_moment = pd.read_excel(file_path, sheet_name='hip_moment')

    para = [hip_angle, knee_angle, ankle_angle, hip_moment, knee_moment, ankle_moment, force]

    knee_a = np.zeros((101, 5))
    knee_m = np.zeros((101, 5))
    ankle_a = np.zeros((101, 5))
    ankle_m = np.zeros((101, 5))
    hip_a = np.zeros((101, 5))
    hip_m = np.zeros((101, 5))
    force_s = np.zeros((101, 5))
    times = np.zeros((5, 7))

    para_avg = [hip_a, knee_a, ankle_a, hip_m, knee_m, ankle_m, force_s]

    for i in range(0, 7):
        for n in range(1, len(para[i].iloc[0, :])):
            for h in range(0, len(Height)):
                if para[i].columns[n].split('.')[0] == Height[h]:
                    num = np.array(para[i].iloc[0:101, n])
                    if i == 6:
                        AX[i].plot(num, color=color_dict[Height[h]], alpha=0.1)
                        AX[i + 1].plot(num, color=color_dict[Height[h]], alpha=0.1)
                        AX[i + 2].plot(num, color=color_dict[Height[h]], alpha=0.1)
                        para_avg[i][:, h] = para_avg[i][:, h] + num
                        times[h, i] = times[h, i] + 1
                    else:
                        AX[i].plot(num, color=color_dict[Height[h]], alpha=0.1)
                        para_avg[i][:, h] = para_avg[i][:, h] + num
                        times[h, i] = times[h, i] + 1
    ax1.legend(handles=handles, ncol=1, loc='upper left')
    plt.show()

    fig2 = plt.figure()
    bx1 = fig2.add_subplot(3, 3, 1)
    plt.title('Hip joint')
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Hip Angle (deg)')
    bx2 = fig2.add_subplot(3, 3, 2)
    plt.title('Knee joint')
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Knee Angle (deg)')
    bx3 = fig2.add_subplot(3, 3, 3)
    plt.title('Ankle joint')
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ankle Angle (deg)')
    bx4 = fig2.add_subplot(3, 3, 4)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Hip Moment (Nm/Kg)')
    bx5 = fig2.add_subplot(3, 3, 5)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Knee Moment (Nm/Kg)')
    bx6 = fig2.add_subplot(3, 3, 6)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ankle Moment (Nm/Kg)')
    bx7 = fig2.add_subplot(3, 3, 7)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ground Reaction Force (N)')
    bx8 = fig2.add_subplot(3, 3, 8)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ground Reaction Force (N)')
    bx9 = fig2.add_subplot(3, 3, 9)
    plt.xlabel('Gait phase (%)')
    plt.ylabel('Ground Reaction Force (N)')

    BX = [bx1, bx2, bx3, bx4, bx5, bx6, bx7, bx8, bx9]

    for i in range(0, 7):
        for h in range(0, len(Height)):
            para_avg[i][:, h] = para_avg[i][:, h] / times[h, i]
            if i == 6:
                BX[i].plot(para_avg[i][:, h], color=color_dict[Height[h]], alpha=1)
                BX[i + 1].plot(para_avg[i][:, h], color=color_dict[Height[h]], alpha=1)
                BX[i + 2].plot(para_avg[i][:, h], color=color_dict[Height[h]], alpha=1)
            else:
                BX[i].plot(para_avg[i][:, h], color=color_dict[Height[h]], alpha=1)
    bx1.legend(handles=handles, ncol=1, loc='upper left')
    plt.show()
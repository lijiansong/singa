import matplotlib.pyplot as plt

def extract_and_plot(log_file_name, net_name):
    pay_load_list = []
    pay_load_list.append(0.0)
    with open(log_file_name, 'r') as mem_info_reader:
        info_list = mem_info_reader.readlines()
        malloc_dict = {}
        current_load = 0.0
        for info in info_list:
            info = info.rstrip('\n')
            #print(info)
            #MALLOC: 0x7f4bfd20b800 819716 1601023543447
            #FREE: 0x7f4bfd20b800 1601023543447
            it_list = info.split(' ')
            if it_list[0] == 'MALLOC:':
                malloc_size = float(it_list[2])/1024.0/1024.0
                current_load += malloc_size
                malloc_dict[it_list[1]] = malloc_size
                pay_load_list.append(current_load)
            if it_list[0] == 'FREE:':
                free_size = malloc_dict[it_list[1]]
                current_load -= free_size
                pay_load_list.append(current_load)
        print('---> {}'.format(len(malloc_dict)))

    x = [i for i in range(len(pay_load_list))]

    l1=plt.plot(x, pay_load_list,'b--',label=net_name)
    plt.ylabel('Memory footprint(/MB)')
    #plt.legend()
    plt.show()

if __name__ == '__main__':
    extract_and_plot('gan-mem-info.log', 'GAN')

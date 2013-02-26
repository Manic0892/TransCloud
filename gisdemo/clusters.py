
br01='cmatthew@' 'PC.transgeo.pgeni-gpolab-bbn-com.wall3.test.ibbt.be'
br02='cmatthew@' 'PC-0.transgeo.pgeni-gpolab-bbn-com.wall3.test.ibbt.be'
br03='cmatthew@' 'PC-1.transgeo.pgeni-gpolab-bbn-com.wall3.test.ibbt.be'
br04='cmatthew@' 'PC-2.transgeo.pgeni-gpolab-bbn-com.wall3.test.ibbt.be'

brussels_cluster = [br01,br02,br03,br04]

grack06 = 'genericuser@grack06.uvic.trans-cloud.net'
grack05 = 'genericuser@grack05.uvic.trans-cloud.net'
grack04 = 'genericuser@grack04.uvic.trans-cloud.net'
grack03 = 'genericuser@grack03.uvic.trans-cloud.net'
grack02 = 'genericuser@grack02.uvic.trans-cloud.net'
grack01 = 'genericuser@grack01.uvic.trans-cloud.net'
sebulba = 'cmatthew@sebulba.cs.uvic.ca'

uvic_cluster =  [sebulba,grack06,grack05,grack04,grack03,grack02,grack01]


emu1='cmatthew@pc283.emulab.net'
emu2='cmatthew@pc320.emulab.net'
emu3='cmatthew@pc297.emulab.net'
emu4='cmatthew@pc303.emulab.net'
emulab_cluster =  [emu1, emu2, emu3, emu4]

all_clusters = [brussels_cluster, uvic_cluster, emulab_cluster] 

# tmp dirs are different at different clusters. 
tmp_dirs = {"cs.UVic.CA":"/tmp/",
            "uvic.trans-cloud.net":"/tmp/",
            "emulab.net":"/mnt/",
            ".ibbt.be":"/mnt/"}

def n_machines():
    """How many machines are there?"""
    n = 0
    for cluster in all_clusters:
        for machine in cluster:
            n += 1
    return n


def test_getclusters():
    assert n_machines() > 0, "Where are the machines?" 


import sys
sys.path.insert(0, './mq/')
import taskmanager
def get_cluster_tmp_location():
    cluster_name = taskmanager.get_local_site_name()
    assert cluster_name in tmp_dirs
    return tmp_dirs[cluster_name]

    
def test_gettmp():
    assert get_cluster_tmp_location() in ['/mnt','/tmp/']
import ci
import ovn_ovs
import flannel


CI_MAP = {
    "ovn-ovs": ovn_ovs.OVN_OVS_CI,
    "flannel": flannel.Flannel_CI
}

def get_ci(name):
    ci_obj = CI_MAP.get(name, ci.CI)
    return ci_obj()
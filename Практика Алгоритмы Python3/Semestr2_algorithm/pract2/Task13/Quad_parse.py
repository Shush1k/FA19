from coeff_a import get as get_a
from coeff_b import get as get_b
from coeff_c import get as get_c
def parse_exp(input_str):
    index_a = get_a(input_str)
    index_b = get_b(input_str)
    index_c = get_c(input_str)
    return list(map(float, [index_a,index_b,index_c]))
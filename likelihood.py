# I have to calculate p(x|ck)
# p(x|ck) = p(x,ck) / p(ck)
# p(x,ck) = p(ck|x)p(x) or p(x and ck)
# so p(x|ck) = p(ck|x)p(x) / p(ck)
# p(ck) means PRIOR
# p(ck|x) means POSTERIOR

def calculate_binary_likelihood(x,f_prior, s_prior):
    f_like = x / f_prior
    s_like = x / s_prior
    return [f_like, s_like]

def calculate_multi_class_likelihood(x, f_prior, s_prior, t_prior, fo_prior):
    f_like = x / f_prior
    s_like = x / s_prior
    t_like = x / t_prior
    fo_like = x / fo_prior
    return [f_like, s_like, t_like, fo_like]
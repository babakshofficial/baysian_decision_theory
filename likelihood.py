# I have to calculate p(x|ck)
# p(x|ck) = p(x,ck) / p(ck)
# p(x,ck) = p(ck|x)p(x)
# so p(x|ck) = p(ck|x)p(x) / p(ck)
# p(ck) means PRIOR
# p(ck|x) means POSTERIOR
def calculate_likelihood(x):

    return [1,2]
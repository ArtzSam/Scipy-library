from scipy.stats import norm, uniform
import numpy as np

mu, sigma = 0, 1
normal_distribution = norm(mu, sigma)

a, b = -2, 2
uniform_distribution = uniform(a, b-a)

values = np.linspace(-3, 3, 5)

pdf_normal = normal_distribution.pdf(values)
pdf_uniform = uniform_distribution.pdf(values)
print("PDF для нормального распределения:", pdf_normal)
print("-----------------")
print("PDF для равномерного распределения:", pdf_uniform)
print("-----------------")

cdf_normal = normal_distribution.cdf(values)
cdf_uniform = uniform_distribution.cdf(values)
print("CDF для нормального распределения:", cdf_normal)
print("-----------------")
print("CDF для равномерного распределения:", cdf_uniform)
print("-----------------")

random_normal = normal_distribution.rvs(size=10)
random_uniform = uniform_distribution.rvs(size=10)
print("Случайные числа из нормального распределения:", random_normal)
print("-----------------")
print("Случайные числа из равномерного распределения:", random_uniform)
print("-----------------")

(pdf_normal, pdf_uniform, cdf_normal, cdf_uniform, random_normal, random_uniform)

from scipy.stats import ttest_1samp

sample_uniform = uniform.rvs(-1, 2, size=10)

t_stat, p_value = ttest_1samp(sample_uniform, 0)

(t_stat, p_value, sample_uniform)

print("Значение t-статистики:", t_stat)
print("-----------------")
print("p-значение:", p_value)
print("-----------------")
print("Выборка из равномерного распределения:", sample_uniform)
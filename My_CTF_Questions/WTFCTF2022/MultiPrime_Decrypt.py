# Solves multi prime rsa given n, e, and c. Need to factor n into primes first (recommend yafu)
# Reference https://crypto.stackexchange.com/questions/31109/rsa-enc-decryption-with-multiple-prime-modulus-using-crt
# From https://github.com/diogoaj/ctf-writeups/tree/master/2018/Timisoara/crypto/NotYourAverageRSA

# Params
e = 65537
c = 10636314778423579441464714144910134843683095093495095563980120464548692638033380133640979847645847952844444379555404880439514247195700794666353076856080304727941831553789250616296025804881674
n = 38578135550447517739542239779708098901080986172879473631654667626197856390371578435993838155329817382415600802660251156126595246342001747411088477515178800507322296738764204516463333876947837
# primes are factored from n
primes = [13791271931, 14045354431, 9135653437, 13351818269, 12139150253, 16755272693, 12624207653, 17085139931, 10173449261, 14433479449, 9864787187, 16512953389, 11924202263, 15640499503, 11824459483, 16610374789, 10802213987, 14984854631, 13227411217, 16593548737, 13898961539, 8883963797, 16733116537, 12405130123, 13370635781, 10965930293, 11279137189, 9312576787, 15410839123, 14616587107, 15424024453, 9190503997, 15975600409, 12580269851]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

ts = []
xs = []
ds = []

for i in range(len(primes)):
	ds.append(modinv(e, primes[i]-1))

m = primes[0]

for i in range(1, len(primes)):
	ts.append(modinv(m, primes[i]))
	m = m * primes[i]

for i in range(len(primes)):
	xs.append(pow((c%primes[i]), ds[i], primes[i]))

x = xs[0]
m = primes[0]

for i in range(1, len(primes)):
	x = x + m * ((xs[i] - x % primes[i]) * (ts[i-1] % primes[i]))
	m = m * primes[i]


print hex(x%n)[2:-1].decode("hex")

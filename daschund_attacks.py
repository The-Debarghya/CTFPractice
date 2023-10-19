import math
import decimal
D = decimal.Decimal

e = D(69927018923298133979974197624968206354916974989080521315929189007456412322941923649962384045930225248936868152215242018290307885829694511113048898103221078978305059093875316375414192628135920237762961812172890732303882748651858700534329101706664951432869349439048734016893248624070673361795079801168014353747)
N = D(100470933740354745428728342046977910357047082422721450692101078016615016493203228246931444845771417062222046523532930918553464001954714745143905289413763465067339607854272315374950175281943116999885968813579942973534265516070715616849327644108251465889788005562440683092014949366143225176350556413380960966567)
c_m = 8708764751442072914257435757464754876714232953849182381575878617890890638100146440058182511127412231140482253903600933621982938101481002901258296318015840672292264406841148283960559066776842721313145879670534579267640966396629754032209389998749271158096258624117151411480429857939832848402047838242943043765

#Continued fraction expansion of e/N (see https://en.wikipedia.org/wiki/Continued_fraction):
n_fe = e #nominator
d_fe = N #denominator
fraction_list = []

def expand_fraction_list(n_fe, d_fe):
    with decimal.localcontext() as ctx:
        ctx.prec = 350    
        cap = math.floor(n_fe/d_fe)
        rest = n_fe%d_fe
        fraction_list.append(cap)
        
        n_fe = d_fe
        d_fe = rest
    return (n_fe, d_fe)

def cfe(a_list, j): #Calculate fraction from fraction_list
    n_next = 0
    d_next = 1
    while j >= 0:
        d = d_next
        k = a_list[j]*d_next+n_next
        n_next = d
        d_next = k
        j = j-1
    return k,d #returns guess for k and d. d is the private key.




#Perform Wieners Attack (see https://en.wikipedia.org/wiki/Wiener%27s_attack)

n_fe, d_fe = expand_fraction_list(n_fe, d_fe) #creates 0th element in fraction list

for i in range(1,1000):   
    n_fe, d_fe = expand_fraction_list(n_fe, d_fe) #adds new element to fraction list
    k,d = cfe(fraction_list, i) #calculates the fraction for the i'th fraction expansion
    with decimal.localcontext() as ctx:
        ctx.prec = 10000
        PhiN = D((e*d-1)/k)
        if PhiN%1 == 0 and d%2 == 1: #Checks if phi(N) is a natural number and if d is odd
            with decimal.localcontext() as ctx: #try to solve square equation x2 + bx + c == 0
                ctx.prec = 1000
                b = -(N-PhiN+1)
                c = N
                sqr2 = b**2-4*c
                if sqr2 > 0: #checks if squareroot therm is larger than 0
                    sqr = D(sqr2.sqrt())
                    if sqr%1 == 0 and ((-b+sqr)/2)%1 == 0 and ((-b-sqr)/2)%1 == 0: #checks if squareroot-therm and the two solutions are all natural numbers
                        break

print("d = ", d)            

N = int(N)

m_c = pow(c_m, d, N)
print("Decrypted message: ", m_c)

from Crypto.Util.number import long_to_bytes
text = long_to_bytes(m_c)

print("Plain text: ", text) 

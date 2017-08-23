for i in range(250) :
    # Replace the comma from the last with a semi colon to comply with CSS syntax
    if i !=249 :
        print( "rgb(18, 128, 106) {}px {}px,".format( i+1 , i+1 ) )
    else :
        print( "rgb(18, 128, 106) {}px {}px;".format( i+1 , i+1 ) )
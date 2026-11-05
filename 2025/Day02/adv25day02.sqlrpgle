**FREE
Ctl-Opt Main(ADV25DAY02);
Ctl-Opt dftactgrp(*no);
Ctl-Opt option(*srcstmt:*nodebugio);

dcl-ds rangeDS_t Qualified Template;
  From packed(15);
  To packed(15);
end-ds;

dcl-enum Bools;
  True '1';
  False '0';
end-enum;


Dcl-Proc ADV25DAY02;
  Dcl-Pi *N;
    p_filepath char(50); // File path on IFS to read input data
  End-Pi;


  dcl-s data varchar(500);
  dcl-s filePath varchar(50);

  dcl-s rangeVarchar varchar(50);
  dcl-ds rangeDS likeDS(rangeDS_t);
  dcl-s from_to_list varchar(25) dim(2);
  dcl-s sumTotal packed(20);

  dcl-s i packed(15);


  filePath = %trim(p_filepath);


  exec sql
    SELECT line
    into :data
    FROM table(qsys2.ifs_read_utf8(path_name => :filePath)) limit 1;

  if sqlcode <> 0;
    snd-msg *info 'SQLCODE <> 0 - Data not Read' %target(*pgmbdy:1) ;
    snd-msg *info 'FilePath: ' + filePath %target(*pgmbdy:1) ;
    return;
  endif;

  sumTotal = *Zeros;

  for-each rangeVarchar in %split(data:',');

    from_to_list = %split(rangeVarchar:'-');
    rangeDS.From = %int(from_to_list(1));
    rangeDS.To = %int(from_to_list(2));

    sumTotal += GetSumOfInvalids(rangeDS);


  endfor;

  snd-msg *info 'sumTotal: ' + %char(sumTotal) %target(*pgmbdy:1) ;
  // snd-msg *info %char(sumTotal) %target(*pgmbdy:1) ;

  return;

End-Proc ADV25DAY02;



Dcl-Proc GetSumOfInvalids;
  Dcl-Pi *N packed(20);
    rangeDS likeDS(rangeDS_t) const;
  End-Pi;

  dcl-s number packed(15);
  dcl-s sumOfInvalids packed(20);

  sumOfInvalids = 0;

  for number=rangeDS.From to rangeDS.To;
    if not isValidNumber(number);
      snd-msg *info 'Invalid: ' + %char(%dec(number:15:0)) %target(*pgmbdy:1) ;
      sumOfInvalids += number;
    endif;
  endfor;

  return sumOfInvalids;


End-Proc GetSumOfInvalids;

dcl-proc isValidNumber;
  dcl-pi *n IND;
    number packed(15) const;
  end-pi;

  dcl-s numberString varchar(15);
  dcl-s firstPart varchar(8);
  dcl-s CompareVal1 varchar(8);
  dcl-s CompareVal2 varchar(8);
  dcl-s splitPos packed(2:0);
  dcl-s isWholeStringRepeating IND;

  dcl-s splitCount packed(2);
  dcl-s splitComparison packed(2);
  dcl-s splitPosDisplace packed(2);

  dcl-s lennumber packed(4);
  dcl-s lennumberstring packed(4);

  numberString = %char(number);

  for splitCount = 2 to %len(numberString);
    lennumber = %len(number);
    lennumberstring = %len(numberString);
    splitPos = %len(numberString) / splitCount;

    if splitPos = 0 or %rem(%len(numberString):splitCount) > 0;
      iter;
    endif;

    firstPart = %subst(numberString:1:splitPos);
    isWholeStringRepeating = True;
    for splitComparison = 1 to splitCount-1;
      // if split into 3 parts, first comparison should not displace, 2nd displace by magnitude of splitPos
      splitPosDisplace = splitPos * (splitComparison-1) ;
      CompareVal1 = %subst(numberString:1+splitPosDisplace:splitPos);
      CompareVal2 = %subst(numberString:1+splitPos+splitPosDisplace:splitPos);

      if firstPart = CompareVal1 and CompareVal1 = CompareVal2 and isWholeStringRepeating;
        isWholeStringRepeating = True;
      else;
        isWholeStringRepeating = False;
        leave;
      endif;
    endfor;

    if isWholeStringRepeating;
      return False;
    endif;

  endfor;

  return True;


  // Part 1 saved

  // value 1 / 2 = 0 -- invalid array below then
  // uneven wont be sequence either
  // if %len(numberString) <= 1;// or %rem(%len(numberString):2) = 1;
  //   return True;
  // endif;

  // halfwayPos = %len(numberString) / 2;

  // dow halfwayPos > 0;
  //   firstHalf = %subst(numberString:1:halfwayPos);
  //   secondHalf = %subst(numberString:halfwayPos+1:halfwayPos);

  //   if firstHalf = secondHalf;
  //     snd-msg *info 'Invalid: ' + numberString %target(*pgmbdy:1) ;
  //     return False;
  //   endif;

  //   halfwayPos -= 1;
  // enddo;
  // return True;




end-proc;

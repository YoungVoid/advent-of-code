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
  dcl-s firstHalf varchar(8);
  dcl-s secondHalf varchar(8);
  dcl-s halfwayPos packed(2:0);

  numberString = %char(number);

  // value 1 / 2 = 0 -- invalid array below then
  // uneven wont be sequence either
  if %len(numberString) <= 1 or %rem(%len(numberString):2) = 1;
    return True;
  endif;

  halfwayPos = %len(numberString) / 2;
  firstHalf = %subst(numberString:1:halfwayPos);
  secondHalf = %subst(numberString:halfwayPos+1);

  if firstHalf = secondHalf;
    snd-msg *info 'Invalid: ' + numberString %target(*pgmbdy:1) ;
    return False;
  else;
    return True;
  endif;


end-proc;


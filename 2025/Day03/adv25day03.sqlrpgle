**FREE
Ctl-Opt Main(ADV25DAY03);
Ctl-Opt dftactgrp(*no);
Ctl-Opt option(*srcstmt:*nodebugio);


dcl-c LINE_LENGTH 100;

Dcl-Proc ADV25DAY03;
  Dcl-Pi *N;
    p_filepath char(50); // File path on IFS to read input data
  End-Pi;


  dcl-s data varchar(LINE_LENGTH);
  dcl-s filePath varchar(50);
  dcl-s mychar char(1) dim(100);

  dcl-s firstIndex packed(3);
  dcl-s secondIndex packed(3);

  dcl-ds numberValue Qualified;
    firstNumber char(1);
    secondNumber char(1);
  end-ds;
  dcl-s total packed(10) inz(0);



  dcl-ds line Qualified;
    digit char(1) dim(LINE_LENGTH);
  end-ds;

  exec sql
    DECLARE c1 CURSOR FOR
    SELECT line FROM table(qsys2.ifs_read_utf8(path_name => :filePath));


  filePath = %trim(p_filepath);

  exec sql open c1;

  exec sql fetch c1 into :data;
  dow sqlcode = 0;

    line = data;

    firstIndex = GetHighestNumberPosition(%subst(line:1:LINE_LENGTH-1));
    numberValue.firstNumber = line.digit(firstIndex);

    secondIndex = GetHighestNumberPosition(%subst(line:firstIndex+1));
    numberValue.secondNumber = line.digit(secondIndex + firstIndex);

    total += %int(numberValue);

    snd-msg *info line + ' | ' + %char(numberValue) %target(*pgmbdy:1) ;

    exec sql fetch c1 into :data;
  enddo;

  snd-msg *info 'Answer: ' + %Char(total) %target(*pgmbdy:1) ;


End-Proc ADV25DAY03;

dcl-proc GetHighestNumberPosition;
  dcl-pi *n packed(3);
    p_line char(LINE_LENGTH) const;
  end-pi;

  dcl-s line varchar(LINE_LENGTH);
  dcl-s number char(1);
  dcl-s highestNumber char(1);
  dcl-s highestNumberIndex packed(3);
  dcl-s index packed(3);
  dcl-s digit char(1);

  line = %trim(p_line);


  if %len(line) = 1;
    return 1;
  endif;

  highestNumber = '';
  for index = 1 to %len(line); //-1 to not count the last
    number = %subst(line:index:1);
    if number > highestNumber;
      highestNumber = number;
      highestNumberIndex = index;
    endif;

    if highestNumber = '9';
      leave;
    endif;
  endfor;

  return highestNumberIndex;


end-proc;

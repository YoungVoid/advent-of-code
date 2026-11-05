**FREE
Ctl-Opt Main(ADV25DAY01);
Ctl-Opt dftactgrp(*no);
Ctl-Opt option(*srcstmt:*nodebugio);


dcl-ds instruction_t Qualified Template;
  direction char(1);
  distance packed(4);
end-ds;

dcl-ds MoveDialDS_t Qualified Template;
  newPosition int(5);
  password_increments int(5);
end-ds;

dcl-pr MoveDial EXTPROC likeds(MoveDialDS_t);
  currentPosition int(5) const;
  instruction likeds(instruction_t) const;
end-pr;



Dcl-Proc ADV25DAY01;
  Dcl-Pi *N;
    p_filepath char(50); // File path on IFS to read input data
  End-Pi;

  dcl-ds instruction likeds(instruction_t);
  dcl-s data varchar(10);

  dcl-s filePath varchar(50);
  dcl-s currentPosition int(5);
  dcl-s password int(5);

  dcl-s tmp varchar(100);

  dcl-ds MoveDialDS likeds(MoveDialDS_t);

  exec sql
    DECLARE c1 CURSOR FOR
    SELECT line FROM table(qsys2.ifs_read_utf8(path_name => :filePath));


  filePath = %trim(p_filepath);
  currentPosition = 50;
  password = 0;

  exec sql open c1;

  exec sql fetch c1 into :data;
  dow sqlcode = 0;
    instruction.direction = %subst(data:1:1);
    instruction.distance = %int(%subst(data:2));

    MoveDialDS = MoveDial(currentPosition:instruction);

    password += MoveDialDS.password_increments;
    currentPosition = MoveDialDS.newPosition;

    exec sql fetch c1 into :data;
  enddo;

  snd-msg *info 'Password: ' + %Char(password) %target(*pgmbdy:1) ;


End-Proc ADV25DAY01;

dcl-proc MoveDial;
  dcl-pi *n likeds(MoveDialDS_t);
    currentPosition int(5) const;
    instruction likeds(instruction_t) const;
  end-pi;

  dcl-s remaining_distance int(5);

  dcl-ds MoveDialDS likeds(MoveDialDS_t);

  clear MoveDialDS;


  remaining_distance = instruction.distance;
  MoveDialDS.newPosition = currentPosition;

  // Need to not count this twice - would already have been counted in the previous instruction.
  if currentPosition = 0 and instruction.direction = 'L';
    MoveDialDS.password_increments -= 1;
  endif;

  if remaining_distance >= 100;
    MoveDialDS.password_increments += %div(instruction.distance:100);
    remaining_distance = %rem(remaining_distance:100);
  endif;

  if instruction.direction = 'L';
    MoveDialDS.newPosition -= remaining_distance;
  else;
    MoveDialDS.newPosition += remaining_distance;
  endif;

  if MoveDialDS.newPosition > 99;
    MoveDialDS.newPosition -= 100;
    MoveDialDS.password_increments +=1;

  elseif MoveDialDS.newPosition < 0;
    MoveDialDS.newPosition += 100;
    MoveDialDS.password_increments +=1;

  elseif MoveDialDS.newPosition = 0;
    MoveDialDS.password_increments += 1;
  endif;

  return MoveDialDS;

end-proc MoveDial;

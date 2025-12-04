**FREE
Ctl-Opt Main(ADV25DAY04);
Ctl-Opt dftactgrp(*no);
Ctl-Opt option(*srcstmt:*nodebugio);

dcl-c TEST_LENGTH 10;
dcl-c INPUT_LENGTH 135;

dcl-c ROW_COUNT 135;
dcl-c COL_COUNT 135;

dcl-ds Grid_t Qualified Template;
  dcl-ds row Dim(ROW_COUNT);
    col char(1) Dim(COL_COUNT);
  end-ds;
end-ds;

Dcl-Proc ADV25DAY04;
  Dcl-Pi *N;
    p_filepath char(50) const; // File path on IFS to read input data
  End-Pi;

  dcl-ds Grid likeds(Grid_t);
  dcl-s answer packed(10);
  dcl-s rollsRemoved packed(10);



  Grid = GetData(p_filepath);

  answer = 0;

  rollsRemoved = RemoveRolls(Grid);
  answer += rollsRemoved;
  dow rollsRemoved > 0;
    rollsRemoved = RemoveRolls(Grid);
    answer += rollsRemoved;
  enddo;


  snd-msg *info 'Answer: ' + %Char(answer) %target(*pgmbdy:1) ;


End-Proc ADV25DAY04;

dcl-proc GetData;
  dcl-pi *n likeds(Grid_t);
    p_filepath char(50) const;
  end-pi;

  dcl-ds Grid likeds(Grid_t);

  dcl-s data varchar(COL_COUNT);
  dcl-s filePath varchar(50);
  dcl-s index packed(5);

  exec sql
    DECLARE c1 CURSOR FOR
    SELECT line FROM table(qsys2.ifs_read_utf8(path_name => :filePath));


  filePath = %trim(p_filepath);

  exec sql open c1;

  index = 0;
  exec sql fetch c1 into :data;
  dow sqlcode = 0;
    index += 1;
    Grid.row(index) = data;

    exec sql fetch c1 into :data;
  enddo;

  return Grid;

  on-exit;
    exec sql close c1;

end-proc GetData;

dcl-proc GetAdjacentCount;
  dcl-pi *n packed(1);
    Grid likeds(Grid_t) const;
    p_rowPos packed(3) const;
    p_colPos packed(3) const;
  end-pi;

  dcl-s adjacentCount Packed(1);
  dcl-s rowPos Packed(3);
  dcl-s colPos Packed(3);
  dcl-s rowPos_i Packed(3);
  dcl-s colPos_i Packed(3);

  dcl-ds adjacentValues Qualified Template;
    dcl-ds row Dim(ROW_COUNT);
      col char(1) Dim(COL_COUNT);
    end-ds;
  end-ds;


  for rowPos_i = p_rowPos-1 to p_rowPos+1;
    for colPos_i = p_colPos-1 to p_colPos+1;
      rowPos = rowPos_i;
      colPos = colPos_i;


      if colPos = p_colPos and rowPos = p_rowPos; // if working with the middle one
        iter;
      else;
        select;
            // if working on top row, going up to bottom row
          when rowPos = 0;
            iter;
            rowPos = ROW_COUNT;

            // if working on bottom row, going down to top row
          when rowPos > ROW_COUNT;
            iter;
            rowPos = 1;
        endsl;


        select;
            // if working on left col, going left to right-most col
          when colPos = 0;
            iter;
            colPos = COL_COUNT;

            // if working on right col, going right to left-most col
          when colPos > COL_COUNT;
            iter;
            colPos = 1;
        endsl;
      endif;

      if Grid.row(rowPos).col(colPos) = '@';
        adjacentCount += 1;
      endif;

    endfor;
  endfor;

  return adjacentCount;
end-proc;

dcl-proc RemoveRolls;
  dcl-pi *n packed(10);
    Grid likeds(Grid_t);
  end-pi;

  dcl-s rollsRemoved packed(10);

  dcl-s rowPos packed(3);
  dcl-s colPos packed(3);
  dcl-s adjacentCount Packed(1);

  for rowPos=1 to ROW_COUNT;
    for colPos=1 to COL_COUNT;
      if Grid.row(rowPos).col(colPos) = '@';
        adjacentCount = GetAdjacentCount(Grid:rowPos:colPos);
        if adjacentCount < 4;
          Grid.row(rowPos).col(colPos) = 'x';
          rollsRemoved += 1;
        endif;
      endif;

    endfor;
  endfor;

  return rollsRemoved;

end-proc RemoveRolls;


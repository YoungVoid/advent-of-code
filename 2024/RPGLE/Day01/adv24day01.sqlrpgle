**FREE

ctl-opt dftactgrp(*no) actgrp(*new);
ctl-opt option(*srcstmt:*nodebugio);
Ctl-Opt Main(ADV24DAY03);


// https://www.rpgpgm.com/2016/01/read-ifs-file-using-rpg.html
// NV note - replaced *n with names for better clarity

dcl-pr OpenFile int(10) extproc('open') ;
  filefilePath pointer value options(*string) ;        // The filePath where the file is to be found in the IFS (pointer).
  fileStatusAndMode int(10) value ;                         // File status flags and access mode for the file when it is opened (integer).
  filePermission uns(10) value options(*nopass) ;  // File permission bytes (unsigned integer).
  outputCCSID uns(10) value options(*nopass) ;     // Output CCSSID (unsigned integer).
  *n uns(10) value options(*nopass) ;              // Not used (unsigned integer).
 end-pr ;

 dcl-pr ReadFile int(10) extproc('read') ;
   fileDescriptor int(10) value ;                  // File descriptor, the file to be read which is a value returned from the open procedure (integer).
   outputPtr pointer value ;                       // Variable into which the bytes read are placed in (pointer).
   readLength uns(10) value ;                      // The number of bytes retrieved. This can be less than the length of the variable when the last read of the file is performed.
 end-pr ;

 dcl-pr CloseFile int(10) extproc('close') ;
   fileDescriptor  int(10) value ;                 // File descriptor, the file to be closed procedure (integer).
 end-pr ;





dcl-c PUZZLE_INPUT_LINE_COUNT 6;
dcl-c PUZZLE_INPUT_FILE_PATH '/home/VOID/AdventOfCode/2024/Day1Test.txt';

dcl-ds input_t qualified;
  left_number packed(5);
  right_number packed(5);
end-ds;

Dcl-Proc ADV24DAY03;
  Dcl-Pi *N;
  End-Pi;

  dcl-ds puzzleInput likeds(input_t) dim(PUZZLE_INPUT_LINE_COUNT);
  dcl-s i int(10);
  dcl-s answer int(10);

  Clear puzzleInput;

  puzzleInput = FormatData(getDataFromFile(PUZZLE_INPUT_FILE_PATH));

  answer = GetAnswerPart1(puzzleInput);

  snd-msg *INFO %char(answer) %target(*CALLER);

  return;

End-Proc;


dcl-proc GetAnswerPart1;
  dcl-pi *n like(totalDistance);
    puzzleInput likeds(input_t) dim(PUZZLE_INPUT_LINE_COUNT);
  end-pi;

  dcl-ds line likeds(input_t);
  dcl-s totalDistance int(10);


  for-each line in puzzleInput;
    totalDistance += %abs(line.left_number - line.right_number);
    snd-msg *INFO (%char(line.left_number) + ' - ' + %char(line.right_number) + ' = ' + %char(totalDistance) ) %target(*CALLER) ;
  endfor;

  return totalDistance;

end-proc GetAnswerPart1;




dcl-proc FormatData;
  dcl-pi *n likeds(formattedData) Dim(PUZZLE_INPUT_LINE_COUNT);
      rawData char(1000) const;
  end-pi;

  dcl-s i int(10);
  dcl-c endOfLine x'25';
  dcl-ds formattedData likeds(input_t) dim(PUZZLE_INPUT_LINE_COUNT);

  dcl-s line char(5);

  clear formattedData;

  i = 0;
  for-each line in %split(rawData:endOfLine);
    i += 1;
    formattedData(i).left_number = %int(%trim(%subst(line:1:1)));
    formattedData(i).right_number = %int(%trim(%subst(line:5:1)));
  endfor;

  return formattedData;
end-proc;


dcl-proc getDataFromFile;
    dcl-pi *n Like(Data);
        filePath char(256) const;
    end-pi;

    // Define constants and standalone variables:
    dcl-c O_RDONLY 1 ;           //Read only
    dcl-c O_TEXTDATA 16777216 ;  //Open in text mode
    dcl-c O_CCSID 32 ;           //CCSID
    dcl-c S_IRGRP 32 ;           //Group authority
    dcl-c sysCCSID 37;
    dcl-s fileDescriptor int(10) ;
    dcl-s Length int(10) ;


    dcl-s Data char(13000) ; // 1000 lines of 13 characters - 5 + 3 + 5

    fileDescriptor = OpenFile(%trim(filePath) : O_RDONLY + O_TEXTDATA + O_CCSID : S_IRGRP : sysCCSID) ;

    if (fileDescriptor < 0) ;
        // TODO: Handle error?
        //returnCode = -1;
        return *blanks;
    endif ;

    Length  = ReadFile(fileDescriptor:%addr(Data):%size(Data)) ;

    return Data;

  on-exit;
    CloseFile(fileDescriptor);

end-proc;


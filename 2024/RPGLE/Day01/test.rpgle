

        dcl-c True = *ON;
        dcl-c False = *OFF;



        dcl-proc Valid_Seat_Column;
            dcl-pi *n IND;
                seat_Column Char(1) const;
            end-pi;

            select seat_Column;
            when-in %list('A':'B':'C':'D':'E':'F':'H');
                return True;
            other;
                return False;
            endsl;

        
        end-proc;

      * History of changes
      * Date        Ver  chgnum Author        Description
      * 2024-06-12  1.0         ChatGPT       Initial version
      * 2024-06-12  1.1  NV001  Nian          Updated seat column validation

     P VALID_SEAT_COLUMN_FX 
     P                 B 
NV001D seatCol         S              1A   CONST
NV001D isValid         S             10   INZ(*OFF)

     C                   EVAL      isValid = *OFF
     C                   SELECT
     C                   WHEN      seatCol = 'A' OR seatCol = 'B' OR seatCol = 'C' OR seatCol = 'D' OR seatCol = 'E' OR seatCol = 'F' OR seatCol = 'H'
     C                   EVAL      isValid = *ON
     C                   OTHER
     C                   EVAL      isValid = *OFF
     C                   ENDSEL
     C                   RETURN    isValid

     P                 E
/*
  Warnings:

  - You are about to drop the column `led5` on the `led` table. All the data in the column will be lost.
  - Added the required column `pwmLed1` to the `led` table without a default value. This is not possible if the table is not empty.
  - Added the required column `pwmLed2` to the `led` table without a default value. This is not possible if the table is not empty.
  - Added the required column `pwmLed3` to the `led` table without a default value. This is not possible if the table is not empty.
  - Added the required column `pwmLed4` to the `led` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "led" DROP COLUMN "led5",
ADD COLUMN     "pwmLed1" TEXT NOT NULL,
ADD COLUMN     "pwmLed2" TEXT NOT NULL,
ADD COLUMN     "pwmLed3" TEXT NOT NULL,
ADD COLUMN     "pwmLed4" TEXT NOT NULL;

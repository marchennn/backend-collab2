/*
  Warnings:

  - Added the required column `led3` to the `led` table without a default value. This is not possible if the table is not empty.
  - Added the required column `led4` to the `led` table without a default value. This is not possible if the table is not empty.
  - Added the required column `led5` to the `led` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "led" ADD COLUMN     "led3" TEXT NOT NULL,
ADD COLUMN     "led4" TEXT NOT NULL,
ADD COLUMN     "led5" TEXT NOT NULL;

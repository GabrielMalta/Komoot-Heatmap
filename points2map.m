clear

[lat, lon] = importfile("points.csv");


geodensityplot(lat,lon, Radius=10)


function [lat, long] = importfile(filename, dataLines)
if nargin < 2
    dataLines = [1, Inf];
end
opts = delimitedTextImportOptions("NumVariables", 2);
opts.DataLines = dataLines;
opts.Delimiter = ",";
opts.VariableNames = ["lat", "long"];
opts.VariableTypes = ["single", "single"];
opts.ExtraColumnsRule = "ignore";
opts.EmptyLineRule = "read";
tbl = readtable(filename, opts);
lat = tbl.lat;
long = tbl.long;
end
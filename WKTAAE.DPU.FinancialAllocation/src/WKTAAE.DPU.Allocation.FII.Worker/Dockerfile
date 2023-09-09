#See https://aka.ms/customizecontainer to learn how to customize your debug container and how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/runtime:6.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.FII.Worker/WKTAAE.DPU.Allocation.FII.Worker.csproj", "WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.FII.Worker/"]
RUN dotnet restore "WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.FII.Worker/WKTAAE.DPU.Allocation.FII.Worker.csproj"
COPY . .
WORKDIR "/src/WKTAAE.DPU.FinancialAllocation/src/WKTAAE.DPU.Allocation.FII.Worker"
RUN dotnet build "WKTAAE.DPU.Allocation.FII.Worker.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "WKTAAE.DPU.Allocation.FII.Worker.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WKTAAE.DPU.Allocation.FII.Worker.dll"]
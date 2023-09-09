using Microsoft.Data.SqlClient;
using Microsoft.Extensions.Options;
using System.Data;

namespace WKTAAE.DPU.Allocation.Repository.Helpers
{
    public class DbContext
    {
        private readonly DbSettings _dbSettings;

        public DbContext(IOptions<DbSettings> dbSettings)
        {
            _dbSettings = dbSettings.Value;
        }

        public IDbConnection CreateSqlConnection()
        {
            return new SqlConnection(_dbSettings.SqlConnection);
        }
    }
}
